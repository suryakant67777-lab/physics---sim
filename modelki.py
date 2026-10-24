import os
import threading
import tkinter as tk
from tkinter import scrolledtext
import pyttsx3
import torch
import torch.nn as nn
from torch.nn import functional as F

# ==========================================
# AUDIO / TTS INITIALIZATION (Fast Female Voice)
# ==========================================
def speak_text(text):
  """Background thread me audio chalayega taaki GUI freeze na ho"""
  def _speak():
    try:
      engine = pyttsx3.init()
      voices = engine.getProperty('voices')
      for voice in voices:
        if "zira" in voice.name.lower() or "female" in voice.name.lower():
          engine.setProperty('voice', voice.id)
          break
      else:
        if len(voices) > 1:
          engine.setProperty('voice', voices[1].id)

      engine.setProperty('rate', 220)  # Fast tapori speech speed
      engine.say(text)
      engine.runAndWait()
    except Exception as err:
      print(f"Audio Error: {err}")

  threading.Thread(target=_speak, daemon=True).start()

# ==========================================
# HYPERPARAMETERS & SETUP
# ==========================================
batch_size = 64
block_size = 64
device = "cuda" if torch.cuda.is_available() else "cpu"
n_embd = 128
n_head = 4
n_layer = 4
dropout = 0.3

print(f"🔥 Using Device: {device}")

# ==========================================
# CHECKPOINT LOADER
# ==========================================
model_path = "tapori_gpt_model.pth"

if not os.path.exists(model_path):
  raise FileNotFoundError(f"❌ Error: '{model_path}' nahi mili! Checkpoint file yahan rakho.")

checkpoint = torch.load(model_path, map_location=device, weights_only=True)

if isinstance(checkpoint, dict) and "model_state_dict" in checkpoint:
  state_dict = checkpoint["model_state_dict"]
  chars = checkpoint["chars"]
  vocab_size = checkpoint["vocab_size"]
else:
  state_dict = checkpoint
  if os.path.exists("mera_hindi_data.txt"):
    with open("mera_hindi_data.txt", "r", encoding="utf-8") as f:
      text = f.read()
    chars = sorted(list(set(text)))
    vocab_size = len(chars)
  else:
    raise ValueError("❌ Checkpoint me 'chars' nahi mile!")

stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for i, ch in enumerate(chars)}
encode = lambda s: [stoi[c] for c in s if c in stoi]
decode = lambda l: "".join([itos[i] for i in l if 0 <= i < len(itos)])

# ==========================================
# GPT MODEL ARCHITECTURE
# ==========================================
class Head(nn.Module):
  def __init__(self, head_size):
    super().__init__()
    self.key = nn.Linear(n_embd, head_size, bias=False)
    self.query = nn.Linear(n_embd, head_size, bias=False)
    self.value = nn.Linear(n_embd, head_size, bias=False)
    self.register_buffer("tril", torch.tril(torch.ones(block_size, block_size)))
    self.dropout = nn.Dropout(dropout)

  def forward(self, x):
    B, T, C = x.shape
    k = self.key(x)
    q = self.query(x)
    wei = q @ k.transpose(-2, -1) * k.shape[-1] ** -0.5
    wei = wei.masked_fill(self.tril[:T, :T] == 0, float("-inf"))
    wei = F.softmax(wei, dim=-1)
    wei = self.dropout(wei)
    v = self.value(x)
    return wei @ v

class MultiHeadAttention(nn.Module):
  def __init__(self, num_heads, head_size):
    super().__init__()
    self.heads = nn.ModuleList([Head(head_size) for _ in range(num_heads)])
    self.proj = nn.Linear(head_size * num_heads, n_embd)
    self.dropout = nn.Dropout(dropout)

  def forward(self, x):
    out = torch.cat([h(x) for h in self.heads], dim=-1)
    return self.dropout(self.proj(out))

class FeedForward(nn.Module):
  def __init__(self, n_embd):
    super().__init__()
    self.net = nn.Sequential(
        nn.Linear(n_embd, 4 * n_embd),
        nn.ReLU(),
        nn.Linear(4 * n_embd, n_embd),
        nn.Dropout(dropout),
    )

  def forward(self, x):
    return self.net(x)

class Block(nn.Module):
  def __init__(self, n_embd, n_head):
    super().__init__()
    head_size = n_embd // n_head
    self.sa = MultiHeadAttention(n_head, head_size)
    self.ffwd = FeedForward(n_embd)
    self.ln1 = nn.LayerNorm(n_embd)
    self.ln2 = nn.LayerNorm(n_embd)

  def forward(self, x):
    x = x + self.sa(self.ln1(x))
    return x + self.ffwd(self.ln2(x))

class GPTLanguageModel(nn.Module):
  def __init__(self):
    super().__init__()
    self.token_embedding_table = nn.Embedding(vocab_size, n_embd)
    self.position_embedding_table = nn.Embedding(block_size, n_embd)
    self.blocks = nn.Sequential(*[Block(n_embd, n_head=n_head) for _ in range(n_layer)])
    self.ln_f = nn.LayerNorm(n_embd)
    self.lm_head = nn.Linear(n_embd, vocab_size)

  def forward(self, idx, targets=None):
    B, T = idx.shape
    tok_emb = self.token_embedding_table(idx)
    pos_emb = self.position_embedding_table(torch.arange(T, device=device))
    x = tok_emb + pos_emb
    x = self.blocks(x)
    x = self.ln_f(x)
    logits = self.lm_head(x)

    if targets is None:
      loss = None
    else:
      B, T, C = logits.shape
      logits = logits.view(B * T, C)
      targets = targets.view(B * T)
      loss = F.cross_entropy(logits, targets)

    return logits, loss

  def generate(self, idx, max_new_tokens, temperature=0.85):
    for _ in range(max_new_tokens):
      idx_cond = idx[:, -block_size:]
      logits, loss = self(idx_cond)
      logits = logits[:, -1, :] / temperature
      probs = F.softmax(logits, dim=-1)
      idx_next = torch.multinomial(probs, num_samples=1)
      idx = torch.cat((idx, idx_next), dim=1)
    return idx

# Initialize Model
model = GPTLanguageModel().to(device)
model.load_state_dict(state_dict)
model.eval()
print("🚀 Haramkhor Neural Engine Online!")

# ==========================================
# GENERATE RESPONSE & CATCH OUTPUT
# ==========================================
def get_model_response(user_input):
  prompt = f"Q: {user_input}\nA:"
  encoded_prompt = encode(prompt)

  if not encoded_prompt:
    return "Arre bsdk dhang se type kar!"

  context = torch.tensor(encoded_prompt, dtype=torch.long, device=device).unsqueeze(0)
  with torch.no_grad():
    generated = model.generate(context, max_new_tokens=90, temperature=0.85)
  full_text = decode(generated[0].tolist())

  try:
    if "A:" in full_text:
      ans_part = full_text.split("A:")[-1]
      if "Q:" in ans_part:
        ans_part = ans_part.split("Q:")[0]
      clean_ans = ans_part.split("\n")[0].strip()
      return clean_ans if clean_ans else "Bol na bhai, aage sun..."
    return full_text.strip()
  except Exception:
    return "Bhai kuch samajh nahi aaya, dubara bol."

def generate_response(event=None):
  user_input = entry.get().strip()
  if not user_input:
    return

  chat_window.config(state=tk.NORMAL)
  chat_window.insert(tk.END, f"YOU: {user_input}\n", "user")

  bot_output = get_model_response(user_input)

  chat_window.insert(tk.END, f"HARAMKHOR: {bot_output}\n\n", "bot")
  chat_window.config(state=tk.DISABLED)
  chat_window.see(tk.END)
  entry.delete(0, tk.END)

  # Voice Synthesis Call
  speak_text(bot_output)

# ==========================================
# FUTURISTIC CYBERPUNK GUI SETUP
# ==========================================
root = tk.Tk()
root.title("🔥 HARAMKHOR AI - Neural Terminal v2.0")
root.geometry("600x720")
root.config(bg="#0b0f19")  # Deep space dark blue/black

# Top Header / Banner Panel
header_frame = tk.Frame(root, bg="#111827", bd=0, relief=tk.FLAT)
header_frame.pack(fill=tk.X, padx=12, pady=12)

title_lbl = tk.Label(
    header_frame,
    text="⚡ HARAMKHOR v2.0 // OFFLINE NEURAL CORE",
    bg="#111827",
    fg="#f87171",
    font=("Segoe UI", 12, "bold"),
)
title_lbl.pack(side=tk.LEFT, padx=12, pady=10)

status_lbl = tk.Label(
    header_frame,
    text=f"🟢 STATUS: ONLINE ({device.upper()})",
    bg="#111827",
    fg="#34d399",
    font=("Segoe UI", 9, "bold"),
)
status_lbl.pack(side=tk.RIGHT, padx=12, pady=10)

# Main Chat Display Frame (Card Style)
chat_container = tk.Frame(root, bg="#111827", bd=0)
chat_container.pack(padx=12, pady=(0, 10), fill=tk.BOTH, expand=True)

chat_window = scrolledtext.ScrolledText(
    chat_container,
    wrap=tk.WORD,
    bg="#0d1117",
    fg="#e5e7eb",
    font=("Consolas", 11),
    bd=0,
    highlightthickness=0,
    padx=12,
    pady=12,
)
chat_window.pack(fill=tk.BOTH, expand=True, padx=4, pady=4)
chat_window.config(state=tk.DISABLED)

# Custom Tags for Cyberpunk Text Coloring
chat_window.tag_config("user", foreground="#60a5fa", font=("Consolas", 11, "bold"))
chat_window.tag_config("bot", foreground="#f43f5e", font=("Consolas", 11, "bold"))

# Bottom Input Panel Card
input_panel = tk.Frame(root, bg="#111827", bd=0)
input_panel.pack(padx=12, pady=12, fill=tk.X)

entry = tk.Entry(
    input_panel,
    font=("Segoe UI", 12),
    bg="#1f2937",
    fg="#ffffff",
    insertbackground="#f87171",
    bd=0,
    relief=tk.FLAT,
)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=10, padx=(12, 8), pady=8)
entry.bind("<Return>", generate_response)

send_btn = tk.Button(
    input_panel,
    text="TRANSMIT 🚀",
    command=generate_response,
    bg="#ef4444",
    fg="#ffffff",
    font=("Segoe UI", 10, "bold"),
    bd=0,
    activebackground="#dc2626",
    activeforeground="#ffffff",
    cursor="hand2",
    padx=16,
    pady=8,
)
send_btn.pack(side=tk.RIGHT, padx=(0, 12), pady=8)

root.mainloop()

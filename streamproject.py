import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.title("PHYSICS SIMULATION",anchor="center")#it is the title of the app
st.header("select a choice from the dropdown menu")#it is the header of the app
option=st.selectbox("Enter your choice",options=['1. PROJECTILE AND GRAPHS',
'2. FRICTION AND GRAPHS',
'3. WORK AND ENERGY',
'4. ROTATIONAL MOTION AND GRAPHS',
'5. GRAVITY AND GRAPHS',
'6. WAVES AND PROPERTIES',
'7. VERNIAR SCALE AND CALIPERS',
'8. EXIT'])#it is the dropdown menu where you can select the option you want to see
st.write("You have selected option",option)
if option=="1. PROJECTILE AND GRAPHS":
    type=st.selectbox("Select the type of projectile",options=['SIMPLE PROJECTILE','HORIZONTAL PROJECTILE'])#it is the dropdown menu where you can select the type of projectile you want to see
    if type=="SIMPLE PROJECTILE":
        st.write("you have selected simple projectile")#it is used to display the text in the streamlit app
        speed=st.number_input("speed:") #it is the input box where you can enter the speed of the projectile
        angle=st.number_input("angle made from horizontal:") #it is the input box where you can enter the angle of the projectile
        t=(((speed)*2)*np.sin(np.radians(angle)))/9.8
        tr=np.linspace(0,t,100000)
        x=speed*np.cos(np.radians(angle))*tr
        y=speed*np.sin(np.radians(angle))*tr-(1/2)*9.8*tr**2
        maxh=((speed*np.sin(np.radians(angle)))**2)/19.6
        maxr=(((speed)**2)*np.sin(2*np.radians(angle)))/9.8
        st.write('Range=',maxr)
        st.write('Maximum height=',maxh)
        st.write("Time of flight=",t)
        mask=y>=0#mask is essentially filter that you apply to an aaray to hide or remove data you donot want to see
        x_plot=x[mask]
        y_plot=y[mask]
        plt.clf()#it is used to clear the current figure before plotting a new one
        plt.grid(True,linewidth=0.5,color='blue')
        fig,ax=plt.subplots()#it is used to display the plot in the streamlit app
        ax.plot(x_plot,y_plot,color='red',linestyle='--')
        ax.set_xlim(0,maxr+5)
        ax.set_ylim(0,maxh+5)
        ax.set_xlabel('horizontal position')
        ax.set_ylabel('vertical position')
        ax.set_title('SIMPLE PROJECTILE')
        ax.grid(True,linewidth=0.5,color='blue')
        st.pyplot(fig)
        st.subheader("Simple Projectile")
        st.write("1.A simple projectile is an object that is thrown or launched into the air and is subject to the force of gravity. The motion of a simple projectile can be analyzed using the principles of kinematics and dynamics. The key parameters that describe the motion of a simple projectile include its initial velocity, launch angle, time of flight, maximum height, and range. The trajectory of a simple projectile follows a parabolic path, and its motion can be described by equations that relate these parameters to each other. Understanding the behavior of simple projectiles is important in various fields, including physics, engineering, and sports.")
        st.write("2.In a simple projectile motion, the object is launched with an initial velocity at a certain angle above the horizontal. The vertical and horizontal components of the velocity can be calculated using trigonometric functions. The time of flight can be determined by analyzing the vertical motion, while the range can be calculated using the horizontal motion. The maximum height is reached when the vertical component of the velocity becomes zero. By understanding these principles, we can predict the trajectory and behavior of a simple projectile under the influence of gravity.")
        st.write("3.The equations of motion for a simple projectile can be derived from the basic kinematic equations. The horizontal and vertical positions of the projectile at any given time can be calculated using the following formulas: x = v0 * cos(theta) * t and y = v0 * sin(theta) * t - (1/2) * g * t^2, where v0 is the initial velocity, theta is the launch angle, g is the acceleration due to gravity, and t is the time. By analyzing these equations, we can determine important characteristics of the projectile's motion, such as its range, maximum height, and time of flight.")
        st.write("4.In summary, a simple projectile is an object that is launched into the air and follows a parabolic trajectory under the influence of gravity. The motion of a simple projectile can be analyzed using kinematic equations, and key parameters such as range, maximum height, and time of flight can be calculated based on the initial velocity and launch angle. Understanding the principles of simple projectile motion is essential in various applications, including physics, engineering, and sports.")
    elif type=="HORIZONTAL PROJECTILE":
        st.write("you have selected horizontal projectile")
        speed=st.number_input("speed:") #it is the input box where you can enter the speed of the projectile
        t=(((speed)*2))/9.8
        tr=np.linspace(0,t,100000)
        h=st.number_input("enter the height:") #it is the input box where you can enter the height of the projectile
        x=speed*tr
        y=h-(1/2)*9.8*tr**2
        maxr=speed*t
        st.write('Range=',maxr)
        st.write("Time of flight=",t)
        mask=y>=0
        x_plot=x[mask]
        y_plot=y[mask]
        plt.grid(True,linewidth=0.5,color='blue')
        fig,ax=plt.subplots()
        ax.plot(x_plot,y_plot,color='red',linestyle='--')
        ax.set_xlabel('horizontal position')
        ax.set_ylabel('vertical position')
        ax.set_title('HORIZONTAL PROJECTILE')
        ax.grid(True,linewidth=0.5,color='blue')
        st.pyplot(fig)
        st.subheader("Horizontal Projectile")
        st.write("1.A horizontal projectile is an object that is launched horizontally from a certain height and is subject to the force of gravity. The motion of a horizontal projectile can be analyzed using the principles of kinematics and dynamics. The key parameters that describe the motion of a horizontal projectile include its initial velocity, time of flight, range, and maximum height. The trajectory of a horizontal projectile follows a parabolic path, and its motion can be described by equations that relate these parameters to each other. Understanding the behavior of horizontal projectiles is important in various fields, including physics, engineering, and sports.")
        st.write("2.In a horizontal projectile motion, the object is launched with an initial velocity  parallel to the horizontal surface. The vertical motion of the projectile is influenced by gravity, while the horizontal motion is constant. The time of flight can be determined by analyzing the vertical motion, while the range can be calculated using the horizontal motion. The maximum height is reached when the vertical component of the velocity becomes zero. By understanding these principles, we can predict the trajectory and behavior of a horizontal projectile under the influence of gravity.")
        st.write("3.The equations of motion for a horizontal projectile can be derived from the basic kinematic equations. The horizontal and vertical positions of the projectile at any given time can be calculated using the following formulas: x = v0 * t and y = h - (1/2) * g * t^2, where v0 is the initial velocity, h is the initial height, g is the acceleration due to gravity, and t is the time. By analyzing these equations, we can determine important characteristics of the projectile's motion, such as its range, maximum height, and time of flight.")
        st.write("4.In summary, a horizontal projectile is an object that is launched horizontally from a certain height and follows a parabolic trajectory under the influence of gravity. The motion of a horizontal projectile can be analyzed using kinematic equations, and key parameters such as range, maximum height, and time of flight can be calculated based on the initial velocity and height. Understanding the principles of horizontal projectile motion is essential in various applications, including physics, engineering, and sports.")  
elif option=="6. WAVES AND PROPERTIES":
    st.write("you have selected waves and properties")
    plt.ion()
    amplitude=st.number_input('enter the amplitude:',value=1.0)#value is the default value of the input box
    time_period=st.number_input("enter the timeperiod:",value=1.0)
    initial_phase=st.number_input("enter the initial phase:",value=0.0)
    angular_frequency=st.number_input("enter the angular frequency:",value=1.0)
    t=st.number_input("enter the time of instant:",value=0.0)
    t1=np.linspace(0,5*time_period,100)
    x1=amplitude*np.sin(angular_frequency*t1+np.radians(initial_phase))   
    x=amplitude*np.sin(angular_frequency*t+np.radians(initial_phase))  
    velocity=amplitude*angular_frequency*np.cos(angular_frequency*t+np.radians(initial_phase))
    acceleration=-amplitude*angular_frequency**2*np.sin(angular_frequency*t+np.radians(initial_phase))
    time_of_instant=np.linspace(-amplitude,amplitude,100)
    st.write("displacement at time of instant:",x)
    st.write('acceleration at time of intant:',acceleration)
    st.write("velocity at time of instant:",velocity )
    fig,ax=plt.subplots()
    ax.plot(time_of_instant,x1,color='red',linewidth=0.5,linestyle='--')
    ax.set_ylabel('displacement')
    ax.set_xlabel('period')
    ax.set_title('WAVE GRAPH')
    ax.grid(True,linewidth=0.5,color='blue')
    st.pyplot(fig)
    st.subheader("Waves and their properties")
    st.write("1.Waves are disturbances that propagate through a medium or space.")
    st.write("2.There are two main types of waves: mechanical waves and electromagnetic waves.")
    st.write("3.Mechanical waves require a medium to travel through, such as air, water, or solid materials. Examples include sound waves and water waves.")
    st.write("4.Electromagnetic waves do not require a medium and can travel through a vacuum. Examples include light waves, radio waves, and X-rays.")
    st.write("5.Waves have several properties, including wavelength, frequency, amplitude, and speed.")
    st.write("6.Wavelength is the distance between two consecutive points in a wave, such as crest to crest or trough to trough.")
    st.write("7.Frequency is the number of wave cycles that pass a given point per unit of time, typically measured in hertz (Hz).")
    st.write("8.Amplitude is the maximum displacement of a wave from its equilibrium position, which determines the wave's energy.")
    st.write("9.Speed is the rate at which a wave propagates through a medium, calculated as the product of wavelength and frequency.")
    st.write("10.The relationship between these properties can be expressed as: speed = wavelength × frequency.")
    st.write("11.Waves can also exhibit phenomena such as reflection, refraction, diffraction, and interference.")
    st.write("12.Reflection occurs when a wave bounces off a surface, while refraction is the bending of a wave as it passes from one medium to another.")
    st.write("13.Diffraction is the bending of waves around obstacles or through openings, and interference is the interaction of two or more waves that can result in constructive or destructive interference.")
    st.write("14.Understanding waves and their properties is essential in various fields, including physics, engineering, and communication technologies.")
elif option=="5. GRAVITY AND GRAPHS":
    st.write("you have selected gravity and graphs")
    plt.ion()
    mass1=st.number_input("enter the mass of first body:",value=1.0)
    mass2=st.number_input("enter the mass of second body:",value=1.0)
    distance=st.number_input("enter the distance between the two bodies:",value=1.0)
    G=6.67*10**(-11)
    force=(G*mass1*mass2)/distance**2
    st.write(f"gravitational force between the two bodies:{force}N")
    gravity_potential_energy=-(G*mass1*mass2)/distance
    st.write(f"gravitational potential energy between the two bodies:{gravity_potential_energy}J")
    grvitational_field_strength1=force/mass2
    st.write(f"gravitational field strength at the location of second body:{grvitational_field_strength1}N/kg")
    grvitational_field_strength2=force/mass1
    st.write(f"gravitational field strength at the location of first body:{grvitational_field_strength2}N/kg")
    fig,ax=plt.subplots()
    distance_values=np.linspace(0.1,distance,100)
    force_values=(G*mass1*mass2)/distance_values**2
    ax.plot(force_values,distance_values,color='red',linewidth=0.5,linestyle='--')
    ax.set_xlabel('gravitational force')
    ax.set_ylabel('distance')
    ax.set_title('GRAVITY')
    ax.grid(True,linewidth=0.5,color='blue')
    st.pyplot(fig)
    st.subheader("Gravity and its properties")
    st.write("1.Gravity is a fundamental force of nature that attracts two masses towards each other.")
    st.write("2.The strength of the gravitational force between two objects is determined by their masses and the distance between them, as described by Newton's law of universal gravitation.")
    st.write("3.The gravitational force can be calculated using the formula: F = G * (m1 * m2) / r^2, where F is the gravitational force, G is the gravitational constant, m1 and m2 are the masses of the two objects, and r is the distance between their centers.")
    st.write("4.Gravitational potential energy is the energy an object possesses due to its position in a gravitational field, calculated as U = -G * (m1 * m2) / r.")
    st.write("5.Gravitational field strength is the force per unit mass experienced by an object in a gravitational field, calculated as g = F / m, where F is the gravitational force and m is the mass of the object.")
    st.write("6.Gravity is responsible for the motion of planets, stars, galaxies, and other celestial bodies, as well as phenomena such as tides and the formation of black holes.")
    st.write("7.Understanding gravity is essential in various fields, including physics, astronomy, and engineering, as it plays a crucial role in the structure and dynamics of the universe.")
elif option=="2. FRICTION AND GRAPHS":
    st.write("you have selected friction and graphs")
    plt.ion()
    mass=st.number_input("enter the mass of the object:",value=1.0)
    coefficient_of_friction=st.number_input("enter the coefficient of friction:",value=0.5)
    normal_force=mass*9.8
    frictional_force=coefficient_of_friction*normal_force
    st.write(f"frictional force acting on the object:{frictional_force}N")
    fig,ax=plt.subplots()
    coefficient_values=np.linspace(0,1,100)
    frictional_force_values=coefficient_values*normal_force
    ax.plot(coefficient_values,frictional_force_values,color='red',linewidth=0.5,linestyle='--')
    ax.set_xlabel('coefficient of friction')
    ax.set_ylabel('frictional force')
    ax.set_title('FRICTION')
    ax.grid(True,linewidth=0.5,color='blue')
    st.pyplot(fig)
    st.subheader("Friction and its properties")
    st.write("1.Friction is a force that opposes the relative motion or tendency of such motion of two surfaces in contact.")
    st.write("2.There are two main types of friction: static friction, which prevents motion from starting, and kinetic friction, which opposes motion that is already occurring.")
    st.write("3.The magnitude of the frictional force can be calculated using the formula: F_friction = μ * F_normal, where F_friction is the frictional force, μ is the coefficient of friction, and F_normal is the normal force exerted by the surface on the object.")
    st.write("4.The coefficient of friction is a dimensionless quantity that represents the ratio of the frictional force to the normal force, and it depends on the materials in contact.")
    st.write("5.Friction plays a crucial role in everyday life, as it allows us to walk without slipping, enables vehicles to grip the road, and is essential for various mechanical processes.")
    st.write("6.Understanding friction is important in fields such as physics, engineering, and materials science, as it affects the design and performance of machines, structures, and transportation systems.")
elif option=="3. WORK AND ENERGY":
    st.write("you have selected work and energy")
    plt.ion()
    mass=st.number_input("enter the mass of the object:",value=1.0)
    velocity=st.number_input("enter the velocity of the object:",value=1.0)
    kinetic_energy=(1/2)*mass*velocity**2
    st.write(f"kinetic energy of the object:{kinetic_energy}J")
    height=st.number_input("enter the height of the object:",value=1.0)
    potential_energy=mass*9.8*height
    st.write(f"potential energy of the object:{potential_energy}J")
    total_energy=kinetic_energy+potential_energy
    st.write(f"total energy of the object:{total_energy}J")
    fig,ax=plt.subplots(1,2,figsize=(10,5))
    velocity_values=np.linspace(0,velocity*2,100)
    kinetic_energy_values=(1/2)*mass*velocity_values**2
    ax[0].plot(velocity_values,kinetic_energy_values,color='red',linewidth=0.5,linestyle='--')
    ax[0].set_xlabel('velocity')
    ax[0].set_ylabel('kinetic energy')
    ax[0].set_title('WORK AND ENERGY')
    ax[0].grid(True,linewidth=0.5,color='blue')
    height_values=np.linspace(0,height*2,100)
    potential_energy_values=mass*9.8*height_values
    ax[1].plot(height_values,potential_energy_values,color='red',linewidth=0.5,linestyle='--')
    ax[1].set_xlabel('height')
    ax[1].set_ylabel('potential energy')
    ax[1].set_title('WORK AND ENERGY')
    ax[1].grid(True,linewidth=0.5,color='blue')
    st.pyplot(fig)
    st.subheader("Work and Energy")
    st.write("1.Work is defined as the transfer of energy that occurs when a force is applied to an object and causes it to move in the direction of the force. The formula for work is W = F * d * cos(theta), where W is work, F is the magnitude of the force, d is the displacement of the object, and theta is the angle between the force and displacement vectors.")
    st.write("2.Energy is the capacity to do work. It exists in various forms, including kinetic energy, potential energy, thermal energy, and more. The total energy of a system is the sum of its kinetic and potential energies.")
    st.write("3.Kinetic energy is the energy an object possesses due to its motion, calculated as KE = (1/2) * m * v^2, where m is the mass of the object and v is its velocity.")
    st.write("4.Potential energy is the energy an object possesses due to its position in a gravitational field, calculated as PE = m * g * h, where m is the mass of the object, g is the acceleration due to gravity, and h is the height of the object above a reference point.")
    st.write("5.The principle of conservation of energy states that energy cannot be created or destroyed, only transformed from one form to another. In a closed system, the total energy remains constant.")
    st.write("6.Understanding work and energy is essential in various fields, including physics, engineering, and everyday life, as it helps us analyze the behavior of objects and systems under the influence of forces and energy transformations.")
elif option=="4. ROTATIONAL MOTION AND GRAPHS":
    st.write("you have selected rotational motion and graphs")
    plt.ion()
    moment_of_inertia=st.number_input("enter the moment of inertia:",value=1.0)
    angular_velocity=st.number_input("enter the angular velocity:",value=1.0)
    angular_acceleration=st.number_input("enter the angular acceleration:",value=1.0)
    time_of_instant=st.number_input("enter the time of instant:",value=0.0)
    torque=moment_of_inertia*angular_acceleration
    st.write(f"torque at time of instant:{torque}Nm")
    angular_momentum=moment_of_inertia*angular_velocity
    st.write(f"angular momentum at time of instant:{angular_momentum}kg*m^2/s")
    fig,ax=plt.subplots()
    angular_velocity_values=np.linspace(0,angular_velocity*2,100)
    angular_momentum_values=moment_of_inertia*angular_velocity_values
    ax.plot(angular_velocity_values,angular_momentum_values,color='red',linewidth=0.5,linestyle='--')
    ax.set_xlabel('angular velocity')
    ax.set_ylabel('angular momentum')
    ax.set_title('ROTATIONAL MOTION AND GRAPHS')
    ax.grid(True,linewidth=0.5,color='blue')
    st.pyplot(fig)
    st.subheader("Rotational Motion and its properties")
    st.write("1.Rotational motion refers to the motion of an object around a fixed axis, where all points in the object move in circles around the axis.")
    st.write("2.The moment of inertia is a measure of an object's resistance to changes in its rotational motion, calculated as I = m * r^2 for point masses, where m is the mass and r is the distance from the axis of rotation.")
    st.write("3.Angular velocity is the rate of change of angular displacement, measured in radians per second (rad/s).")
    st.write("4.Angular acceleration is the rate of change of angular velocity, measured in radians per second squared (rad/s^2).")
    st.write("5.Torque is the measure of the force that causes an object to rotate, calculated as τ = I * α, where τ is torque, I is the moment of inertia, and α is the angular acceleration.")
    st.write("6.Angular momentum is the rotational analog of linear momentum, calculated as L = I * ω, where L is angular momentum, I is the moment of inertia, and ω is the angular velocity.")
    st.write("7.Understanding rotational motion is essential in various fields, including physics, engineering, and mechanics, as it helps us analyze the behavior of rotating objects and systems under the influence of torques and angular momentum.")
elif option=="7. VERNIAR SCALE AND CALIPERS":
    plt.ion()
    main_scale_length=st.number_input("enter the length of one main scale division:", min_value=0.0, value=1.0)
    verniar_scale_length=st.number_input("enter the length of one verniar scale division:", min_value=0.0, value=1.0)
    number_of_verniar_divisions=st.number_input("enter the number of divisions on the verniar scale:", min_value=1, value=10)
    least_count=main_scale_length/number_of_verniar_divisions
    print(f"least count of the verniar calipar:{least_count}cm")
    fig,ax=plt.subplots()
    ax.set_xlabel('number of divisions on verniar scale')
    ax.set_ylabel('least count')
    ax.set_title('VERNIAR CALIPAR')
    divisions_values=np.arange(1,number_of_verniar_divisions+1)
    least_count_values=main_scale_length/divisions_values
    ax.plot(divisions_values,least_count_values,color='red',linewidth=0.5,linestyle='--')
    ax.grid(True,linewidth=0.5,color='blue',alpha=0.5)
    st.pyplot(fig)
    st.write("you have selected verniar scale and calipers")
    st.subheader("Verniar Scale and Calipers")
    st.write("1.A vernier scale is a precise measuring instrument used to measure linear dimensions with high accuracy. It consists of a main scale and a sliding vernier scale that allows for measurements to be read to a fraction of the smallest division on the main scale.")
    st.write("2.Calipers are tools used to measure the distance between two opposite sides of an object. They can be used to measure internal and external dimensions, as well as depths. There are different types of calipers, including vernier calipers, dial calipers, and digital calipers.")
    st.write("3.Vernier calipers have a main scale and a vernier scale that allows for measurements to be read with high precision, typically to 0.02 mm or 0.001 inches.")
    st.write("4.Dial calipers have a dial gauge that provides a direct reading of the measurement, while digital calipers have an electronic display that shows the measurement in either metric or imperial units.")
    st.write("5.Understanding how to use vernier scales and calipers is essential in various fields, including engineering, manufacturing, and scientific research, as they allow for accurate measurements of objects and components.")
elif option=="8. EXIT":
    st.write("exiting the program...")
    st.stop()
st.write("THANKS OF MR SURYA KANT FOR DEVELOPING THIS APP")
st.subheader("Thank you for using the physics simulation app!")




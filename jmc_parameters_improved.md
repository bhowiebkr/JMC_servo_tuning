# JMC Servo Parameters (Improved Extraction)

## P00-00

**Parameter Name:** Motor number 0-65535 2000 Stop & reset Re-power on

**Description:** No description available

---

## P00-01

**Parameter Name:** rated speed Set range: 1~6000 rpm; unit：rpm; default value.

**Description:** No description available

---

## P00-02

**Parameter Name:** rated torque Set range 0.01-655.35 N.m;unit：N.M default value.

**Description:** No description available

---

## P00-03

**Parameter Name:** Rated current Set range: 0.01-655.35A,unit：A Default value

**Description:** No description available

---

## P00-04

**Parameter Name:** Rotor inertia Set range: 0.01-655.35kg.cm²; unit：kg.cm² Default value

**Description:** No description available

---

## P00-07

**Parameter Name:** Encoder option Range: 0-3 0&1: incremental encoder

**Description:** No description available

---

## P00-08

**Parameter Name:** Line-saving incremental encoder Range: 0-1 0: non line-saving; 1: line-saving;

**Description:** No description available

---

## P00-09

**Parameter Name:** Absolute encoder Range: 0-1 0: Tamagawa encoder 1: Nikon encoder

**Description:** No description available

---

## P00-10

**Parameter Name:** Incremental encoder lines Default set

**Description:** No description available

---

## P00-11

**Parameter Name:** incremental encoder Z pulse electric angle Default set

**Description:** No description available

---

## P00-12

**Parameter Name:** Rotor initial angle 1 Default set

**Description:** No description available

---

## P00-13

**Parameter Name:** Rotor initial angle 2 Default set

**Description:** No description available

---

## P00-14

**Parameter Name:** Rotor initial angle 3 Default set

**Description:** No description available

---

## P00-15

**Parameter Name:** Rotor initial angle 4 Default set

**Description:** No description available

---

## P00-16

**Parameter Name:** Rotor initial angle 5 Default set

**Description:** No description available

---

## P00-17

**Parameter Name:** Rotor initial angle 6 Default set

**Description:** No description available

---

## P00-20

**Parameter Name:** Display settings on power-on interface 0-100 100 --- Running & setting Re-power on

**Description:** No description available

---

## P00-21

**Parameter Name:** RS232 Communication baud rate 0-3 2 --- Running & setting Re-power on

**Description:** No description available

---

## P00-23

**Parameter Name:** Slave address 0-255, default 1 Set according to the equipment requirements

**Description:** No description available

---

## P00-24

**Parameter Name:** Modbus Communication baud rate Set range: 0-7, default 20：2400 1：4800 2：9600 3：19200 4：38400 5：57600 6：115200 7：25600

**Description:** No description available

---

## P00-25

**Parameter Name:** Check way Set range: 0-3, default 0

**Description:** No description available

---

## P00-26

**Parameter Name:** modbus Communication response delay Set range: 0-100; default:0. Response standard while set value is 0; And will response related to the value while it be set.

**Description:** No description available

---

## P00-28

**Parameter Name:** Modbus compatible Set range:0-2; Default:1. 0: Reserve. 1: default 2: Compatible with Chisu protocol （OX11and 16E address）

**Description:** No description available

---

## P00-29

**Parameter Name:** Modbus absolute encoder feedback style set range: 0-1; default: 0. Read absolute position value 84D/84E. 0: 84D is cycle amount. 84E is single cycle amount. 1: 84D is single cycle amount. 84E is cycle amount.

**Description:** No description available

---

## P00-30

**Parameter Name:** Braking resistor setting Set range: 0-2. 0: inside resistor. 1: use outside resistor. 2: No braking resistor.

**Description:** No description available

---

## P00-31

**Parameter Name:** Outsider braking resistor power 0-65536, Unit: 10W.

**Description:** No description available

---

## P00-32

**Parameter Name:** Outsider braking resistor value Setting range :0-1000 Unit: ohm. Set value according to outsider braking resistor

**Description:** No description available

---

## P00-33

**Parameter Name:** regeneration open circuit, Short-circuit detection enable 0-1; 0: Close regeneration open-circuit 1: Open regeneration open-circuit,short-circuit detection enable.

**Description:** No description available

---

## P00-40

**Parameter Name:** Over temperature protection setting 0-1 0: Close over temperature protection 1: Open over temperature protection

**Description:** No description available

---

## P00-41

**Parameter Name:** Control power failure protection settings 0-1 0: Close control power failure protection 1: Open control power failure protection

**Description:** No description available

---

## P00-46

**Parameter Name:** Speed inconsistency alarm detection time setting 0-65536; Unit: ms. 0: Close speed inconsistency alarm detection function. 1-65535: Speed inconsistency alarm detection time setting, When the speed error reaches

**Description:** No description available

---

## P01-01

**Parameter Name:** control mode setting 0-6 0 --- Stop & resetting Real time

**Description:** No description available

---

## P01-02

**Parameter Name:** is set to 1, 2, or 3. It can be called directly according to the actual situation. The larger the set value, the stronger the rigidity.

**Description:** No description available

---

## P01-03

**Parameter Name:** Unknown

**Description:** Automatically adjust the rigidity setting Setting range: 0-31 Built-in 32 kinds of gain parameters. It works when

---

## P01-04

**Parameter Name:** Unknown

**Description:** = Load inertia / motor inertia This inertia ratio can use the value after AF-J-L automatic inertia recognition, write the recognized value into the parameter

---

## P01-10

**Parameter Name:** Control method after overtravel 0-1 0: The motor is in a free state after overtravel, and only receives signals running in the opposite direction 1: The motor is locked after overtravel and only receives signals in the opposite direction.

**Description:** No description available

---

## P01-20

**Parameter Name:** Dynamic brake delay Unit:ms. When the braking conditions are met, the dynamic brake action delay time

**Description:** No description available

---

## P01-21

**Parameter Name:** Disable dynamic brake when main power is off 0-1; 0: Open dynamic brake function 1: Close dynamic brake function

**Description:** No description available

---

## P01-22

**Parameter Name:** Disable dynamic brake when servo OFF. 0-1 0: Open dynamic brake function; 1: Close dynamic brake function.

**Description:** No description available

---

## P01-23

**Parameter Name:** Disable dynamic brake when fault alarm. 0-1 0: Open dynamic brake function; 1: Close dynamic brake function.

**Description:** No description available

---

## P01-24

**Parameter Name:** Disable dynamic brake when overtravel 0-1 0-1 0: Open dynamic brake function; 1: Close dynamic brake function.

**Description:** No description available

---

## P01-30

**Parameter Name:** is executed under the enable command is executed. When the enable is off: When the motor is at a static state, after the close enable command is executed, the time after the brake is closed and the motor becomes non-energized.

**Description:** No description available

---

## P01-31

**Parameter Name:** Speed limit value of brake command output 0-3000, unit: rpm Motor speed threshold when the brake output is active when the motor is rotating. Less than this threshold, the brake output command is valid, otherwise it will wait for

**Description:** No description available

---

## P01-32

**Parameter Name:** Servo OFF-brake command waiting time 0-255, unit: ms The maximum waiting time for the brake output when the motor is rotating.

**Description:** No description available

---

## P01-40

**Parameter Name:** out of control check ENA 0-1 1 --- Running & setting Real time Gain paremeter

**Description:** No description available

---

## P02-00

**Parameter Name:** position control gain 1 0-3000.0 48.0 1/S Running & setting Real time

**Description:** No description available

---

## P02-01

**Parameter Name:** Velocity control gain2 0-3000.0 80.0 ▸ The larger the setting value, the higher the gain, the greater the rigidity, and the smaller the position lag, but if the value is too large, the system will shake and overshoot. ▸ Increase the value as much as possible without shake. ▸ For gain at dynamic.

**Description:** No description available

---

## P02-03

**Parameter Name:** Unknown

**Description:** Speed feedforward gain Setting range: 0-100.0, unit: 1.0% The feedforward gain of the speed loop. The larger the parameter value set, the smaller the system position tracking error and the faster the response. However, if the feedforward gain is too large, the position loop of the system will be unstable, which will easily cause overshoot and vibration.

---

## P02-04

**Parameter Name:** Unknown

**Description:** Speed feedforward smoothing constant Setting range: 0-64.00, unit: ms This parameter is used to set the speed loop feedforward filtering time constant. The larger the value set, the larger the filtering effect, but at the same time the phase lag increases.

---

## P02-10

**Parameter Name:** Unknown

**Description:** 1Speed proportional gain 1 Setting range: 1.0-2000.0, unit: Hz The larger the speed proportional gain is, the larger the servo stiffness is and the faster the speed response is. However, if it is too large, it is easy to generate vibration and noise. Under the condition that the system does not oscillate, increase this parameter value as much as possible. This parameter is for a static response.

---

## P02-11

**Parameter Name:** Unknown

**Description:** Speed integral constant 1 Setting range: 1.0-1000, Unit: ms. Speed regulator integration time constant. The smaller the setting value, the faster the integration speed, the greater the stiffness, and the vibration is too easy to produce noise if it is too small. When the system does not oscillate, reduce this parameter value as much as possible. This parameter is for steady state response.

---

## P02-12

**Parameter Name:** 1 fix to the 2nd gain

**Description:** No description available

---

## P02-13

**Parameter Name:** Unknown

**Description:** speed proportional gain2 Setting range: 1.0-2000.0, unit: Hz The larger the speed proportional gain is, the larger the servo stiffness is and the faster the speed response is. However, if it is too large, it is easy to generate vibration and noise. Under the system has no vibration, increase this parameter value as much as possible. This parameter is for dynamic response.

---

## P02-14

**Parameter Name:** Unknown

**Description:** Speed integral constant 2 Setting range: 1.0-1000.0, unit: ms Speed regulator integration time constant. The smaller the setting value, the faster the integration speed, the greater the stiffness is, and the vibration is too easy to produce noise if it is too small. Under the system has no vibration, reduce this parameter value as much as possible. This parameter is for dynamic response.

---

## P02-15

**Parameter Name:** 2 Use DI input switching Need to set the DI port to 9 (gain switching input) Invalid: first gain Effective: second gain 3 Big torque command value When the torque command is greater than the threshold (determined by

**Description:** No description available

---

## P02-16

**Parameter Name:** Speed integral error limit value 0-32767 Speed integral error limit value

**Description:** No description available

---

## P02-19

**Parameter Name:** Torque feedforward 0-30000, unit: 1.0%

**Description:** No description available

---

## P02-20

**Parameter Name:** Unknown

**Description:** Torque feed-forward smoothing constant Setting range: 0-64.00, unit: ms This parameter is used to set the torque feedforward filtering time constant.

---

## P02-30

**Parameter Name:** Gain switching mode 0-10 The condition to set the 1st and 2nd gain switching mode value Switching condition Remark 0 fix to the 1st gain

**Description:** No description available

---

## P02-31

**Parameter Name:** and

**Description:** No description available

---

## P02-32

**Parameter Name:** Gain switching lag 0-20000 100 --- Running & Real time

**Description:** No description available

---

## P02-33

**Parameter Name:** Gain switching delay 0-1000.0, unit: ms When switching from the second gain to the first gain, the time from when the trigger condition is met to the actual switching.

**Description:** No description available

---

## P02-40

**Parameter Name:** Mode switch selection 0-4 0 --- Running & setting Real time

**Description:** No description available

---

## P02-41

**Parameter Name:** Mode switch selection 0-20000 10000 --- Running & setting Real time

**Description:** No description available

---

## P02-50

**Parameter Name:** Torque command added value -100.0-100, unit: 1.0% Valid in position control mode. This value is superimposed on the torque reference value and is used for vertical axis static torque compensation.

**Description:** No description available

---

## P02-51

**Parameter Name:** Forward torque compensation -100.0-100.0, unit: 1.0% Valid in position control mode. For compensating forward static friction

**Description:** No description available

---

## P02-52

**Parameter Name:** Reverse torque compensation -100.0-0 0 1.0％ Running & setting Real time

**Description:** No description available

---

## P03-00

**Parameter Name:** Source of position command 0：pulse command 1：Given the number, use it when communicating with control

**Description:** No description available

---

## P03-01

**Parameter Name:** Command pulse mode 0：Quadrature pulse command (90°phase difference two-phase pulse) 1： Direction+ pulse command 2or 3:Double pulse command（CW+CCW）

**Description:** No description available

---

## P03-02

**Parameter Name:** Instruction pulse input terminal 0-1 0 0: low speed pulse 1: high-speed pulse

**Description:** No description available

---

## P03-03

**Parameter Name:** Reverse the command pulse 0-1 0 Set the initial direction of motor rotation

**Description:** No description available

---

## P03-06

**Parameter Name:** Location complete range Set range:0-65535 Unit: encoder unit Use to set a threshold value for positioning completion output. When the absolute value motor is used, the encoder is calculated at 131072 bit per turn. Using incremental encoder motor, each turn is calculated by the number of encoder lines * 4.

**Description:** No description available

---

## P03-09

**Parameter Name:** 309 135 465 Number of command pulses for motor rotation

**Description:** No description available

---

## P03-10

**Parameter Name:** 310 136 466 Electronic gear molecules

**Description:** No description available

---

## P03-11

**Parameter Name:** 311 137 467 The electronic gear denominator

**Description:** No description available

---

## P03-12

**Parameter Name:** Electron Gear 1 molecular high position Set range :0-32767 Use this can expand the Electronic gear ratio Molecule value=

**Description:** No description available

---

## P03-13

**Parameter Name:** Electronic gear. 2 molecules See

**Description:** No description available

---

## P03-14

**Parameter Name:** Electronic gear. 2 Denominator See

**Description:** No description available

---

## P03-15

**Parameter Name:** Excessive position deviation setting 0-65535 30000 指令单位*10 Running & setting Real time

**Description:** No description available

---

## P03-22

**Parameter Name:** Increment encoder output pulse frequency division ratio molecule When using incremental encoder, set the number of output pulses of cN1 port.

**Description:** No description available

---

## P03-23

**Parameter Name:** Delta encoder output pulse frequency divider

**Description:** No description available

---

## P03-25

**Parameter Name:** Absolute number of output pulses per revolution of the motor 0-60000 2500 --- Running & setting Real time

**Description:** No description available

---

## P03-30

**Parameter Name:** LINEAR encoder Set the grating ruler Input A, b phase sequence is reversed NO yes

**Description:** No description available

---

## P03-31

**Parameter Name:** Unknown

**Description:** The polarity of the LINEAR ENCODER Z pulse 0-1 1 --- Stop & reset Real time

---

## P03-40

**Parameter Name:** Source of output pulse 0-3 1 --- Stop & reset Real time

**Description:** No description available

---

## P03-42

**Parameter Name:** 0-1 1 --- Stop & Real time

**Description:** No description available

---

## P03-45

**Parameter Name:** Digital quantity instruction cache mode 0-1 0: No caching (immediate execution) 1: CACHING (new data executed after last data execution)

**Description:** No description available

---

## P03-46

**Parameter Name:** Maximum speed of motor at digital position command run time 0-6000 1000 --- Running & setting Real time

**Description:** No description available

---

## P03-50

**Parameter Name:** Unknown

**Description:** The Gantry function enables 0-1 0 --- Stop & setting Real time

---

## P03-51

**Parameter Name:** Unknown

**Description:** The input signal of Gantry function is reversed 0-1 0 --- Stop & setting Real time

---

## P03-52

**Parameter Name:** Number of feedback pulses per turn of Gantry Motor 0-65535 10000 --- Running & setting Re-power on

**Description:** No description available

---

## P03-53

**Parameter Name:** Gantry function position deviation too large settings 0-65535 10000 --- Running & setting Real time

**Description:** No description available

---

## P03-55

**Parameter Name:** Gantry proportional gain 0-200 10 --- Running & setting Real time

**Description:** No description available

---

## P03-60

**Parameter Name:** Origin regression enable control 0-6 0 --- Running & setting Real time

**Description:** No description available

---

## P03-61

**Parameter Name:** Origin regression model 0-9 0 --- Running & setting Real time

**Description:** No description available

---

## P03-65

**Parameter Name:** High speed searching for origin switch 0-1000 100 --- Running & setting Real time

**Description:** No description available

---

## P03-66

**Parameter Name:** Low speed searching for origin switch 0-200 10 --- Running & setting Real time

**Description:** No description available

---

## P03-67

**Parameter Name:** Search origin switch acceleration and deceleration time 0-5000 0 --- Running & setting Real time

**Description:** No description available

---

## P03-68

**Parameter Name:** Maximum time limit for searching origin 0-65550 0 --- Running & setting Real time

**Description:** No description available

---

## P03-69

**Parameter Name:** HMechanical Origin Offset H 0-65535 0 --- Running & setting Real time

**Description:** No description available

---

## P03-70

**Parameter Name:** Mechanical Origin Offset L 0-65535 0 --- Running & setting Real time

**Description:** No description available

---

## P04-00

**Parameter Name:** is set to 1,

**Description:** No description available

---

## P04-01

**Parameter Name:** Speed instruction analog counter 0-1 0 --- Stop & setting Real time

**Description:** No description available

---

## P04-02

**Parameter Name:** is the speed control setting

**Description:** No description available

---

## P04-03

**Parameter Name:** set to 1 B: Speed instruction absolute value less than

**Description:** No description available

---

## P04-04

**Parameter Name:** Zero speed position clamp speed threshold

**Description:** No description available

---

## P04-05

**Parameter Name:** Overspeed alarm value 0-6500 6400 1rpm Running & setting Real time Speed par amet erSpeed par amet er

**Description:** No description available

---

## P04-06

**Parameter Name:** Forward speed limit Set range：0-6000，Unit：rpm Limit forward speed of motor

**Description:** No description available

---

## P04-07

**Parameter Name:** Reverse speed limit Set range：-6000-0，Unit：rpm Limit reverse speed of motor

**Description:** No description available

---

## P04-10

**Parameter Name:** Zero velocity Set range：0-200.0，Unit：rpm 0-6000, unit: rpmSetting speed instruction threshold to trigger zero speed position clamp function

**Description:** No description available

---

## P04-11

**Parameter Name:** Rotation detection value Set range：0-200.0，Unit：rpm Set Motor rotation detection threshold, motor rotation speed higher than the value can be displayed through the LED panel status

**Description:** No description available

---

## P04-12

**Parameter Name:** Consistent range of velocity Set range：0-200.0，Unit：rpm Set speed consistent signal threshold value, when motor speed and instruction speed difference in the threshold value range, can output "speed consistent output" signal through the output port

**Description:** No description available

---

## P04-14

**Parameter Name:** Acceleration time Set range：0-10000，Unit：1ms/1000rpm Set the acceleration time in speed control

**Description:** No description available

---

## P04-15

**Parameter Name:** deceleration time Set range：0-10000，Unit：1ms/1000rpm Set the deceleration time in speed control

**Description:** No description available

---

## P04-30

**Parameter Name:** 1 0 0

**Description:** No description available

---

## P04-31

**Parameter Name:** 0 1 0

**Description:** No description available

---

## P04-32

**Parameter Name:** 1 1 0

**Description:** No description available

---

## P04-33

**Parameter Name:** 0 0 1

**Description:** No description available

---

## P04-34

**Parameter Name:** 1 0 1

**Description:** No description available

---

## P04-35

**Parameter Name:** 0 1 1

**Description:** No description available

---

## P04-36

**Parameter Name:** 1 1 1

**Description:** No description available

---

## P04-37

**Parameter Name:** Internal set speed 8 -6000—6000 0 1rpm Running & setting Real time

**Description:** No description available

---

## P05-00

**Parameter Name:** is set to 1

**Description:** No description available

---

## P05-01

**Parameter Name:** Inverse Torque instruction analog Used to adjust the Torque Direction 0: Normal 1: Direction reverse

**Description:** No description available

---

## P05-02

**Parameter Name:** Torque mode speed limit given value 0-5000 1500 1rpm Running & setting Real time

**Description:** No description available

---

## P05-03

**Parameter Name:** 280 118 430 The digital torque is given

**Description:** No description available

---

## P05-05

**Parameter Name:** Torque limiter source Source for adjusting Torque Limits 0: Internal Digital (set by

**Description:** No description available

---

## P05-06

**Parameter Name:** Torque limit check out delay 0-10000, unit: Ms Setting DO port output torque limit detection output signal delay time

**Description:** No description available

---

## P05-10

**Parameter Name:** If the DI function is not assigned, the system default torque limit value is

**Description:** No description available

---

## P05-11

**Parameter Name:** Internal reverse torque limit unit: 1.0% limit motor reverse output, 100 means 1 times Torque, 300 means 3 times torque when the torque output reaches the limit value, the output signal can be detected

**Description:** No description available

---

## P05-12

**Parameter Name:** Invalid Internal Limited value

**Description:** No description available

---

## P05-13

**Parameter Name:** invalid Internal Limited value

**Description:** No description available

---

## P06-00

**Parameter Name:** DI1Effective level of input port Set range：0-4，Factory set:0 Set valid input of di1 input port of cN1 0: valid for low level (optocoupler on) 1: Valid for high level (optocoupler off) 2: Rising edge effective 3: Falling edge effective 4: Both rising and falling edge are effective

**Description:** No description available

---

## P06-01

**Parameter Name:** DI1 input port function selection (Servo ON) 0-24 1 --- Running & setting Re-power on

**Description:** No description available

---

## P06-02

**Parameter Name:** DI2Effective level of input port see

**Description:** No description available

---

## P06-03

**Parameter Name:** DI2 Function choose of input port see

**Description:** No description available

---

## P06-04

**Parameter Name:** DI3 Valid power level of input port see

**Description:** No description available

---

## P06-05

**Parameter Name:** DI3 Function choose of input port see

**Description:** No description available

---

## P06-06

**Parameter Name:** DI4 Effective level of input port see 06-00

**Description:** No description available

---

## P06-07

**Parameter Name:** DI4 Function choose of input port see

**Description:** No description available

---

## P06-08

**Parameter Name:** DI5 Effective level of input port see

**Description:** No description available

---

## P06-09

**Parameter Name:** DI5 Function choose of input port see

**Description:** No description available

---

## P06-10

**Parameter Name:** DI6 Effective level of input port see

**Description:** No description available

---

## P06-11

**Parameter Name:** DI6 Function choose of input port see

**Description:** No description available

---

## P06-12

**Parameter Name:** DI7 Effective level of input port see

**Description:** No description available

---

## P06-13

**Parameter Name:** DI7 Function choose of input port see

**Description:** No description available

---

## P06-16

**Parameter Name:** DI8 Effective level of input port see

**Description:** No description available

---

## P06-17

**Parameter Name:** DI8 Function choose of input port see

**Description:** No description available

---

## P06-20

**Parameter Name:** DO1 Effective level of input port Set range：0-1， factory set:1 0: When the State is valid, optocoupler cut-off 1: When the State is valid, optocoupler on

**Description:** No description available

---

## P06-21

**Parameter Name:** DO1 Function change of output port (fault:serve ready) 0-13 3 --- Running & setting Re-power on

**Description:** No description available

---

## P06-22

**Parameter Name:** DO2 Effective level of input port see

**Description:** No description available

---

## P06-23

**Parameter Name:** DO2 Function choose of output port see

**Description:** No description available

---

## P06-24

**Parameter Name:** DO3 Function choose of output port see

**Description:** No description available

---

## P06-25

**Parameter Name:** DO3 Function choose of output port see

**Description:** No description available

---

## P06-26

**Parameter Name:** DO4 Function choose of output port see

**Description:** No description available

---

## P06-27

**Parameter Name:** DO4 Function choose of output port see

**Description:** No description available

---

## P06-28

**Parameter Name:** DO5 Function choose of output port see

**Description:** No description available

---

## P06-29

**Parameter Name:** DO5 Function choose of output port see

**Description:** No description available

---

## P06-40

**Parameter Name:** Speed analog command input gain 10-2000 300 1rpm/V Running & setting Real time

**Description:** No description available

---

## P06-41

**Parameter Name:** Speed analog command filter constant Set range：0－64.00，Unit ：ms Set the time factor of analog instruction filtering for CN1 input

**Description:** No description available

---

## P06-42

**Parameter Name:** Velocity analog instruction offset Set range：-10.000－10.000，Unit : V Set The simulated instruction zero offset for CN1 input

**Description:** No description available

---

## P06-43

**Parameter Name:** Torque simulation instruction gain Set range：0－100.0，Unit 1% Set the coefficient between the analog command input by cN1 and the speed control command For example, 30.0 represents 30% of rated torque per V

**Description:** No description available

---

## P06-44

**Parameter Name:** Torque analog instruction filter constant Set range：0－64.00，Unit ：ms Set the time factor of analog instruction filtering for CN1 input

**Description:** No description available

---

## P06-45

**Parameter Name:** Torque analog instruction offset Set range：-10.000－10.000，Unit V Set The simulated instruction zero offset for CN1 input

**Description:** No description available

---

## P06-46

**Parameter Name:** Speed analog instruction dead zone Set range：0－10.000，Unit V Set the dead time voltage value of the speed analog command. When the analog quantity is set within the range of the positive and negative values, the system will default to zero

**Description:** No description available

---

## P06-47

**Parameter Name:** Torque analog instruction dead zone 0-10.000 0 1V Running & setting Real time

**Description:** No description available

---

## P08-01

**Parameter Name:** Load rotation routine identification mode Set range：0-1 0：valid 1：invalid

**Description:** No description available

---

## P08-02

**Parameter Name:** Maximum speed of inertia identification Set range：100-2000，Unit：rpm The maximum speed of the motor in off-line inertia identification

**Description:** No description available

---

## P08-03

**Parameter Name:** Inertia identification acceleration and deceleration time Set range：20-800，Unit：ms The acceleration and deceleration time of motor when off-line inertia identification

**Description:** No description available

---

## P08-04

**Parameter Name:** set conditions automatically generated the value of the rotation circle

**Description:** No description available

---

## P08-05

**Parameter Name:** Unknown

**Description:** The number of motor rotations required to complete a single inertia This parameter is based on

---

## P08-11

**Parameter Name:** Unknown

**Description:** Adaptive notch mode selection Set range：0-4 0: The parameters of the third and fourth notch are no longer automatically updated and are saved to the current value. However, manual input of 1:1 adaptive notch filter is valid, and the parameters of the third notch filter are automatically updated. Manual input of 2:2 adaptive notch filter is valid, and the parameters of the third and fourth notch filters are automatically updated, can Not Manually Input 3: Only Detect Resonance Frequency

---

## P08-13

**Parameter Name:** Unknown

**Description:** Vibration detection threshold of adaptive notch filter Set range：0-7 This parameter sets the vibration detection sensitivity of adaptive notch filter, and the smaller the parameter value, the more sensitive the detection sensitivity is

---

## P08-17

**Parameter Name:** Speed monitor 0-2 0 Running & setting Real time

**Description:** No description available

---

## P08-19

**Parameter Name:** Feedback speed low-pass filter constant Set range：0-25.00，Unit：ms Feedback speed low-pass filter time constant, when the motor running when there is a howling, the value can be set up properly

**Description:** No description available

---

## P08-20

**Parameter Name:** Torque command filter constant1 Set range：0-25.00，Unit：ms Torque instruction filter time constant 1, when there is a motor running, the value can be appropriately set to large.

**Description:** No description available

---

## P08-21

**Parameter Name:** Torque command filter constant2 Set range：0-25.00，Unit：ms Torque instruction filter time constant 2, when there is a motor running, the value can be set appropriately large.

**Description:** No description available

---

## P08-25

**Parameter Name:** Disturbance torque compensation gain Set range：0-100.0 Observed Gain Coefficient of disturbing torque. The larger the value is, the stronger the anti-disturbance Torque is, but the action noise may also be increased.

**Description:** No description available

---

## P08-26

**Parameter Name:** Disturbance torque filtering time constant Set range：0-25.00，Unit：ms The bigger the value is, the stronger the filtering effect is, and the action noise can be suppressed. However, if the disturbance is too large, the phase delay will result and the disturbance torque will be suppressed.

**Description:** No description available

---

## P08-30

**Parameter Name:** Notch Filter 1 frequency Set Range: Set Range: 300-5000, Unit: HZ Notch 1 center frequency Set to 5000, notch invalid

**Description:** No description available

---

## P08-31

**Parameter Name:** Notch Filter 1 width Set range：0-20

**Description:** No description available

---

## P08-32

**Parameter Name:** Unknown

**Description:** Notch Filter 1 depth Set range：0-99 The notch depth grade of Notch 1 is the ratio between the central frequency input and output of Notch 1. The larger the parameter, the smaller the notch depth and the weaker the effect

---

## P08-33

**Parameter Name:** Notch Filter 2 frequency same as

**Description:** No description available

---

## P08-34

**Parameter Name:** Notch Filter 2 width same as

**Description:** No description available

---

## P08-35

**Parameter Name:** Notch Filter 2 depth same as

**Description:** No description available

---

## P08-36

**Parameter Name:** Notch Filter 3 frequency same as

**Description:** No description available

---

## P08-37

**Parameter Name:** Notch Filter 3 width same as

**Description:** No description available

---

## P08-38

**Parameter Name:** Notch Filter 3 depth same as

**Description:** No description available

---

## P08-39

**Parameter Name:** Notch Filter 4 frequency same as

**Description:** No description available

---

## P08-40

**Parameter Name:** Notch Filter 4 width same as

**Description:** No description available

---

## P08-41

**Parameter Name:** Notch Filter 4 depth same as

**Description:** No description available

---


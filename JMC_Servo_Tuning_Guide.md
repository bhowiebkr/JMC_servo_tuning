# JMC Servo Tuning Guide - Buzz Elimination for Position Control

## Overview
This guide provides a systematic approach to eliminate servo buzzing/vibration when operating in position control mode. The buzzing typically indicates excessive gain settings, resonance issues, or inadequate filtering.

## JMC Servo Tuning Philosophy & Best Practices

### The Intelligent Servo Approach
JMC servos are engineered as intelligent drive systems with sophisticated automatic tuning algorithms built into their core functionality. Unlike basic servo drives that require extensive manual parameter adjustment, JMC servos can analyze your mechanical system dynamics, measure load characteristics, and automatically optimize all control loop parameters for peak performance. This intelligent approach represents decades of servo application experience distilled into adaptive algorithms that continuously monitor and adjust system behavior in real-time.

The fundamental philosophy behind JMC servo design is that the drive should adapt to your application, not the other way around. When properly configured, these servos can automatically handle the complex interactions between position control gains, speed loop dynamics, current limiting, and mechanical resonance suppression. This eliminates the traditional trial-and-error approach to servo tuning and reduces setup time from hours or days to minutes.

### System Identification: The Foundation of Optimal Performance
The cornerstone of effective JMC servo tuning begins with accurate system identification, particularly the load-to-motor inertia ratio. This single, critical measurement allows the servo's internal algorithms to calculate optimal gains for all three nested control loops: current control, speed control, and position control. The automatic inertia identification function (AF-JL) not only measures this ratio but also analyzes system dynamics, friction characteristics, and mechanical coupling stiffness.

Once the servo understands your mechanical system through proper inertia identification, it can automatically set hundreds of internal parameters that would otherwise require expert-level knowledge to optimize manually. This includes not just the obvious gain settings, but also integral time constants, derivative actions, feedforward compensation, and filtering characteristics. The servo essentially becomes a tuning expert that knows your specific application.

### Progressive Rigidity: Balancing Performance and Stability  
JMC's automatic rigidity adjustment system (P01-02 modes 1-3) provides pre-calculated gain combinations that have been optimized for different application categories. These rigidity levels represent the culmination of extensive testing across thousands of real-world servo applications, from high-precision positioning systems to high-speed packaging equipment. Each rigidity setting balances multiple competing factors: positioning accuracy, dynamic response speed, system stability, and vibration suppression.

The rigidity scale (P01-03, ranging 0-31) allows fine-tuning within each automatic mode, providing 32 different performance points that span from ultra-smooth operation suitable for delicate mechanisms to high-performance settings for demanding industrial applications. The key advantage is that each rigidity level maintains optimal relationships between all control parameters - something nearly impossible to achieve through manual adjustment without extensive servo expertise.

### Adaptive Control Features: Intelligence That Learns Your System
Modern JMC servos incorporate adaptive control technologies that continuously monitor system behavior and automatically adjust to changing conditions. The adaptive notch filter system can detect mechanical resonance frequencies in real-time and automatically configure filtering to suppress vibrations without degrading servo response. This is particularly valuable in applications where resonance characteristics change due to load variations, temperature effects, or mechanical wear over time.

The servo's vibration detection algorithms analyze torque command ripple, speed feedback noise, and current consumption patterns to identify problematic frequencies before they cause audible buzzing or mechanical stress. When combined with the adaptive filtering system, this creates a servo that becomes quieter and smoother over time as it learns and adapts to your specific mechanical system characteristics.

### Hierarchical Control Architecture: The Engineering Foundation
JMC servos employ a sophisticated three-loop control architecture where each loop operates at different time scales and serves distinct functions. The innermost current control loop operates at the highest frequency (typically 8-16 kHz) and provides precise torque regulation with fast transient response. The middle speed control loop operates at intermediate frequency (1-4 kHz) and regulates motor velocity while providing disturbance rejection. The outermost position control loop operates at the lowest frequency (250-1000 Hz) and provides accurate positioning with appropriate dynamic response.

This hierarchical structure means that tuning must proceed from the inside out - current loop parameters affect speed loop stability, and speed loop characteristics directly impact position loop performance. The automatic tuning modes handle these complex interactions seamlessly, ensuring that each loop operates at its optimal frequency and gain settings while maintaining overall system stability. Manual tuning requires deep understanding of these interdependencies and can easily create unstable interactions if not done correctly.

## Problems with Your Current Manual Configuration

### Bypassing Built-in Intelligence: The Core Issue
Your current servo configuration (P01-02=0, manual rigidity mode) effectively bypasses all of the sophisticated automatic tuning capabilities that make JMC servos intelligent drives. This is analogous to purchasing a modern smartphone with advanced features like GPS navigation, automatic camera settings, and intelligent battery management, then choosing to use it only as a basic calculator. While it will perform the basic function, you're not utilizing any of the advanced engineering that makes the device truly capable.

In manual mode, the servo operates with fixed, predetermined gain settings that cannot adapt to your specific 2.5:1 inertia ratio, your particular mechanical coupling characteristics, or the dynamic requirements of your application. The servo essentially becomes "blind" to system conditions and operates with generic parameters that may or may not be appropriate for your setup. This explains why you're experiencing buzzing - the servo is using aggressive control settings without the complementary filtering, load adaptation, or dynamic response optimization that automatic modes provide.

### Expert Knowledge Requirements and the Rigidity Problem
Manual servo tuning is one of the most complex aspects of motion control engineering, requiring deep understanding of control theory, mechanical system dynamics, electrical noise characteristics, and extensive experience with servo applications across different industries. The current high rigidity setting (P01-03=13) creates an aggressive control response that demands precise coordination between position gains, speed loop parameters, integral time constants, derivative actions, and multiple filtering stages.

Without this expert knowledge, the high rigidity setting becomes counterproductive - the servo is essentially "fighting itself" with overly aggressive gains that create rapid control actions, amplify system noise, generate excessive torque ripple, and excite mechanical resonances. The buzzing you're experiencing is the audible manifestation of these poorly matched control parameters. The servo is trying to achieve precise control with brute force rather than intelligent adaptation, resulting in the mechanical vibrations that create the characteristic servo "buzz" or "whine."

## Quick Reference - Common Buzz Fixes

**Immediate Actions for Buzzing:**
1. **Enable automatic rigidity:** P01-02 from 0→1 (Critical for manual mode buzzing)
2. **Reduce rigidity level:** P01-03 from 13→8 (Lower for smoother operation)
3. **Add torque filtering:** P08-20 = 1.5ms, P08-21 = 1.5ms  
4. **Enable adaptive notch:** P08-11 = 1, P08-13 = 3
5. **Add speed filtering:** P08-19 = 1.0ms

**Emergency Stop Conditions:**
- Excessive vibration or unusual noise
- Servo overheating (>80°C)
- Loss of position control
- Mechanical binding or collision risk

## Prerequisites
- Servo system properly wired and configured
- Motor parameters correctly set:
  - **P00-01** (Motor rated speed): Set to motor nameplate RPM
  - **P00-02** (Motor rated torque): Set to motor nameplate torque (N.m)
  - **P00-03** (Motor rated current): Set to motor nameplate current (A)
  - **P00-04** (Motor rotor inertia): Set to motor specification (kg.cm²)
- Position control mode enabled (P01-01 = 0)
- Electronic gear ratio properly configured (P03-10, P03-11)
- Safety systems in place and tested

## Current Configuration Analysis

### Your System Status (Based on Parameter File)
**Current Critical Settings:**
- **P01-02** = 0 (Manual rigidity adjustment) - **PRIMARY BUZZ CAUSE**
- **P01-03** = 13 (Medium-high rigidity level) - Contributing to buzzing
- **P01-04** = 2.50 (Load inertia ratio) - Well within normal range
- **Motor Configuration**: 3000 RPM, 1.27 N.m, 2.36A rated - Properly configured

**Immediate Problem**: Your servo is in manual rigidity mode (P01-02=0) with a relatively high rigidity setting (P01-03=13). This combination often causes buzzing because:
1. Manual mode doesn't automatically adapt gains to load conditions
2. Fixed high rigidity creates aggressive control response
3. No automatic filtering based on system dynamics

### Recommended Immediate Changes
**Step 1 - Enable Automatic Mode:**
- Change **P01-02**: 0 → 1 (Enable automatic rigidity adjustment)
- This allows the servo to automatically optimize gains based on your inertia ratio

**Step 2 - Reduce Rigidity Level:**
- Change **P01-03**: 13 → 8 (Start conservative, can increase later)
- This reduces control aggressiveness while maintaining acceptable performance

**Step 3 - Add Essential Filtering:**
- **P08-20** (Torque filter 1): Set to 1.5ms
- **P08-21** (Torque filter 2): Set to 1.5ms  
- **P08-19** (Speed feedback filter): Set to 1.0ms

**Step 4 - Enable Vibration Suppression:**
- **P08-11** (Adaptive notch mode): Set to 1 (Single adaptive notch)
- **P08-13** (Vibration threshold): Set to 3 (Medium sensitivity)

**Expected Result:** Immediate reduction in buzzing while maintaining position control accuracy.

## Step-by-Step Buzzing Elimination Procedure

### Phase A: Critical Parameter Changes (Do These First)
**⚠️ SAFETY: Ensure servo is disabled before making parameter changes**

1. **Enable Automatic Rigidity Control:**
   ```
   Parameter: P01-02
   Current Value: 0 (Manual)
   New Value: 1 (Standard automatic mode)
   Reason: Allows servo to auto-optimize gains for your 2.5:1 inertia ratio
   ```

2. **Reduce Rigidity Level:**
   ```
   Parameter: P01-03  
   Current Value: 13 (Medium-high)
   New Value: 8 (Conservative starting point)
   Reason: Reduces control aggressiveness to eliminate buzzing
   ```

3. **Enable Servo and Test:**
   - Turn on servo and listen for buzzing
   - If buzzing eliminated, proceed to Phase B
   - If buzzing remains, continue with filtering

### Phase B: Add Filtering (If Buzzing Continues)

4. **Add Torque Command Filtering:**
   ```
   Parameter: P08-20 (Torque filter 1)
   Set Value: 1.5 ms
   
   Parameter: P08-21 (Torque filter 2) 
   Set Value: 1.5 ms
   
   Effect: Smooths torque commands to reduce high-frequency noise
   ```

5. **Add Speed Feedback Filtering:**
   ```
   Parameter: P08-19 (Speed feedback filter)
   Set Value: 1.0 ms
   Effect: Filters speed feedback to reduce noise-induced vibration
   ```

6. **Test Again:**
   - Enable servo and check for buzzing
   - Move to several positions to test throughout range
   - If stable, proceed to Phase C

### Phase C: Enable Adaptive Vibration Suppression

7. **Enable Adaptive Notch Filter:**
   ```
   Parameter: P08-11 (Adaptive notch mode)
   Set Value: 1 (Single adaptive notch filter)
   
   Parameter: P08-13 (Vibration detection threshold)
   Set Value: 3 (Medium sensitivity)
   
   Effect: Automatically detects and suppresses resonance frequencies
   ```

8. **Final System Test:**
   - Run servo through full motion range
   - Check for any remaining vibration or unusual noise
   - Monitor servo temperature during operation
   - Test positioning accuracy

### Phase D: Performance Optimization (After Buzzing is Eliminated)

9. **Gradually Increase Performance:**
   ```
   If system is stable with P01-03 = 8:
   - Try P01-03 = 10, test for buzzing
   - If stable, try P01-03 = 12, test again
   - Stop at highest value that maintains smooth operation
   ```

10. **Fine-tune Filtering (Optional):**
    ```
    If performance is acceptable, try reducing filters slightly:
    - P08-20, P08-21: Reduce from 1.5ms to 1.0ms
    - P08-19: Reduce from 1.0ms to 0.8ms
    - Test after each change
    ```

**Success Criteria:**
- ✅ No audible buzzing or vibration
- ✅ Smooth motion throughout travel range  
- ✅ Acceptable positioning accuracy
- ✅ Servo temperature within normal range (<60°C)
- ✅ No unusual noise during operation

## Phase 1: System Assessment & Basic Setup

### Step 1.1: Run Automatic Inertia Identification
**Purpose:** Get accurate load-to-motor inertia ratio for optimal tuning

**Procedure:**
1. Set **P08-01 = 0** (Enable load rotation routine identification)
2. Set **P08-02 = 800** (Maximum identification speed - adjust based on your system)
   - Reduce if load has travel limits or high inertia
   - Range: 100-2000 RPM
3. Set **P08-03 = 100** (Acceleration/deceleration time in ms)
   - Increase for high-inertia loads to prevent excessive torque
4. **SAFETY:** Ensure load can rotate freely without collision
5. Execute **AF-JL** function from servo display
6. Wait for completion (typically 10-30 seconds)
7. Note the calculated value and set **P01-04** to this value

**Expected Result:** P01-04 should contain the measured inertia ratio (typically 1.0 to 10.0)
**If identification fails:** Check mechanical coupling, reduce P08-02, or increase P08-03

### Step 1.2: Enable Automatic Rigidity Adjustment
**Purpose:** Let the servo automatically optimize basic gain settings

**Parameters:**
- **P01-03 = 1 to 3** (Start with 1 for conservative, 3 for aggressive)
- Higher values = more rigid/responsive but potentially more buzzing
- Lower values = smoother but potentially less accurate

### Step 1.3: Check Initial Position Control Gains
**Current Default Values:**
- **P02-00** (Position gain 1): Default ~48.0 (1/S)
- **P02-01** (Position gain 2): Default ~80.0

**If buzzing occurs immediately:** Proceed to Phase 2

## Phase 2: Gain Reduction Strategy

### Step 2.1: Reduce Position Loop Gains
**Purpose:** Lower the position control stiffness to eliminate buzz

**Systematic Reduction:**

1. **Reduce P02-00 (Position Control Gain 1):**
   - Current: 48.0 → Try: 30.0
   - Range: 0-3000.0 (1/S)
   - Effect: Lower = less stiff, potentially less buzzing

2. **Reduce P02-01 (Position Control Gain 2):**
   - Current: 80.0 → Try: 50.0
   - Range: 0-3000.0
   - Effect: Lower = less aggressive dynamic response

**Test After Each Change:**
- Enable servo and observe for buzzing
- Move to several positions to test throughout range
- Check position tracking accuracy with encoder feedback
- Note any improvement in buzz amplitude/frequency
- **Record successful values** for later reference

### Step 2.2: Adjust Speed Loop Gains (If Buzzing Persists)
**Purpose:** Fine-tune the inner speed control loop

**Speed Proportional Gains:**
- **P02-10** (Speed proportional gain 1): Range 1.0-2000.0 Hz
  - Start: Reduce by 20% from current value
  - Effect: Lower = less speed loop stiffness
  
- **P02-13** (Speed proportional gain 2): Range 1.0-2000.0 Hz
  - Start: Reduce by 20% from current value
  - For dynamic response tuning

**Speed Integral Constants:**
- **P02-11** (Speed integral constant 1): Range 1.0-1000.0 ms
  - Start: Increase by 50% from current value
  - Higher = slower integration, smoother response
  
- **P02-14** (Speed integral constant 2): Range 1.0-1000.0 ms
  - Start: Increase by 50% from current value
  - For dynamic response tuning

## Phase 3: Add Filtering

### Step 3.1: Enable Torque Command Filtering
**Purpose:** Smooth torque commands to reduce high-frequency noise

**Parameters:**
- **P08-20** (Torque command filter constant 1):
  - Range: 0-25.00 ms
  - Recommended: Start with 1.0-2.0 ms
  - Higher = more filtering, less noise, but slower response

- **P08-21** (Torque command filter constant 2):
  - Range: 0-25.00 ms  
  - Recommended: Start with 1.0-2.0 ms
  - Should match P08-20 initially

### Step 3.2: Add Speed Feedback Filtering
**Purpose:** Filter speed feedback to reduce noise-induced vibration

**Parameter:**
- **P08-19** (Feedback speed low-pass filter):
  - Range: 0-25.00 ms
  - Recommended: Start with 0.8-1.5 ms
  - Description: "When motor running has howling, this value can be set up properly"

**Warning:** Too much filtering can cause instability - start small and increase gradually.

## Phase 4: Vibration Suppression

### Step 4.1: Enable Adaptive Notch Filter
**Purpose:** Automatically detect and suppress resonance frequencies

**Parameters:**
- **P08-11** (Adaptive notch mode selection):
  - Set to **1** (Single adaptive notch filter active)
  - Range: 0-4
  - Options:
    - 0: Manual notch only
    - 1: One adaptive notch active
    - 2: Two adaptive notches active
    - 3: Detect resonance frequency only
    - 4: Clear and reset notch parameters

- **P08-13** (Vibration detection threshold):
  - Range: 0-7
  - Recommended: Start with **3-4**
  - Lower values = more sensitive detection
  - Higher values = less sensitive detection

### Step 4.2: Manual Notch Filter (If Adaptive Fails)
**Purpose:** Manually suppress known problem frequencies

**Identify Problem Frequency:**
1. Use oscilloscope or servo monitoring to identify buzz frequency
2. Common ranges: 300-1500 Hz for mechanical resonance

**Manual Notch Settings:**
- **P08-30** (Notch Filter 1 frequency): 
  - Range: 300-5000 Hz
  - Set to identified problem frequency
  
- **P08-31** (Notch Filter 1 width):
  - Range: 0-20
  - Start with 2-5 (wider = more aggressive filtering)
  
- **P08-32** (Notch Filter 1 depth):
  - Range: 0-99
  - Start with 50-80
  - Lower values = deeper notch (more suppression)

## Phase 5: Fine Tuning & Optimization

### Step 5.1: Optimize Performance vs. Stability
**Goal:** Achieve maximum performance without buzzing

**Procedure:**
1. **Gradually increase gains** from Phase 2 settings:
   - Increase P02-00 by 10% increments
   - Test for buzzing after each change
   - Stop when buzzing begins, then back off 20%

2. **Reduce filtering gradually** from Phase 3 settings:
   - Decrease filter constants by 0.2ms increments  
   - Monitor for return of buzzing
   - Find minimum filtering needed

### Step 5.2: Verify System Performance
**Tests to Perform:**
1. **Position Accuracy:** Check positioning repeatability
2. **Settling Time:** Measure time to reach target position
3. **Following Error:** Monitor during motion
4. **Temperature:** Ensure servo doesn't overheat
5. **Long-term Stability:** Run for extended periods

### Step 5.3: Advanced - Dual Gain Mode (Optional)
**Purpose:** Use different gains for static vs. dynamic conditions

**When to Use:**
- Need high stiffness during motion but smooth holding
- Large inertia loads with varying dynamic requirements

**Setup:**
1. **Configure gain switching:** P02-30 (gain switching mode)
   - 0: Use gain set 1 only (default)
   - 1: Use gain set 2 only
   - 2: DI input switching (requires DI port setup)
   - 3: Large torque command triggers gain set 2

2. **Tune both gain sets:**
   - Gain Set 1: P02-00, P02-01, P02-10, P02-11 (static/holding)
   - Gain Set 2: P02-12, P02-13, P02-14 (dynamic/motion)

3. **Set switching parameters:**
   - P02-32 (gain switching lag): Delay before switching
   - P02-33 (gain switching delay): Time delay for switching

## Troubleshooting Common Issues

### Issue: Buzzing in Manual Rigidity Mode (Your Current Configuration)
**Root Cause:** P01-02 = 0 (Manual mode) with P01-03 = 13 (high rigidity)

**Immediate Solutions:**
1. **Enable automatic mode:** P01-02 = 0 → 1 (Most effective fix)
2. **Reduce rigidity:** P01-03 = 13 → 8 (Conservative starting point)
3. **Add filtering immediately:**
   - P08-20 = 1.5ms (Torque filter 1)
   - P08-21 = 1.5ms (Torque filter 2) 
   - P08-19 = 1.0ms (Speed filter)
4. **Enable adaptive notch:** P08-11 = 1, P08-13 = 3

**Why This Happens:**
- Manual mode uses fixed gains regardless of load conditions
- High rigidity (13/31) creates aggressive control response
- No automatic adaptation to your 2.5:1 inertia ratio
- Missing critical filtering for smooth operation

**Progressive Tuning After Fix:**
1. Test with P01-02=1, P01-03=8 first
2. If stable, gradually increase P01-03 to 10, then 12
3. Monitor for return of buzzing at each step
4. Stop at highest stable rigidity level

### Issue: Buzzing Persists After All Tuning
**Possible Causes & Solutions:**
1. **Mechanical resonance:** Check coupling, mounting, belt tension
2. **Excessive load inertia:** Re-run AF-JL, verify P01-04 calculation
3. **Poor grounding:** Check electrical connections, shield integrity
4. **Encoder issues:** Verify encoder signals, check for noise/interference
5. **Power supply noise:** Check DC bus ripple, add line filters
6. **Worn mechanical components:** Inspect bearings, couplings, guides

### Issue: Poor Position Accuracy After Tuning
**Solutions:**
1. **Increase position gains gradually** (P02-00, P02-01)
2. **Reduce integral time constants** (P02-11, P02-14)
3. **Add feedforward** (P02-03 speed feedforward, 0-100%)
4. **Check mechanical backlash** and electronic gear ratios (P03-10, P03-11)
5. **Verify positioning complete range** (P03-06)

### Issue: Oscillation During Motion
**Solutions:**
1. **Reduce derivative action** (increase integral constants)
2. **Add more filtering** (P08-19, P08-20, P08-21)
3. **Check load coupling stiffness** and mechanical resonance
4. **Reduce position gains** if oscillation is severe
5. **Enable adaptive notch filters** (P08-11)

### Issue: Servo Overheats During Tuning
**Solutions:**
1. **Reduce gains** to lower continuous torque demand
2. **Check load friction** and mechanical binding
3. **Verify current limits** are appropriate for motor
4. **Improve cooling** or reduce duty cycle
5. **Check power supply capacity**

### Issue: Erratic or Jumpy Motion
**Solutions:**
1. **Check encoder connections** and signal quality
2. **Verify electronic gear ratios** (P03-10, P03-11)
3. **Add command smoothing/filtering** 
4. **Check for EMI/noise sources**
5. **Increase integral time constants** for smoother response

## Parameter Backup & Restore

### Before Starting Tuning:
1. **Record all current parameter values**
2. **Save to servo internal memory**
3. **Document working combinations**

### Parameter Documentation Template:
```
Date: ___________
Application: ___________
Load Type: ___________
Inertia Ratio: ___________

Motor Parameters (Current Values from Parameter File):
P00-01: 3000 (Motor rated speed, RPM)
P00-02: 1.27 (Motor rated torque, N.m)
P00-03: 2.36 (Motor rated current, A)
P00-04: 0.34 (Motor rotor inertia, kg.cm²)

Critical Tuning Parameters:
P01-02: _____ (Auto adjust mode: 0=Manual, 1=Standard auto) [Current: 0→Change to 1]
P01-03: _____ (Rigidity setting, 0-31) [Current: 13→Change to 8]
P01-04: 2.50 (Load inertia ratio) [Current: Good]
P02-00: _____ (Position gain 1, 1/S) [Auto-set when P01-02=1]
P02-01: _____ (Position gain 2, 1/S) [Auto-set when P01-02=1]
P02-10: _____ (Speed prop gain 1, Hz) [Auto-set when P01-02=1]
P02-11: _____ (Speed integral 1, ms) [Auto-set when P01-02=1]
P02-13: _____ (Speed prop gain 2, Hz) [Auto-set when P01-02=1]
P02-14: _____ (Speed integral 2, ms) [Auto-set when P01-02=1]

Filtering & Vibration (Add These for Buzzing):
P08-11: _____ (Adaptive notch mode, 0-4) [Recommend: 1]
P08-13: _____ (Vibration threshold, 0-7) [Recommend: 3]
P08-19: _____ (Speed filter, ms) [Recommend: 1.0]
P08-20: _____ (Torque filter 1, ms) [Recommend: 1.5]
P08-21: _____ (Torque filter 2, ms) [Recommend: 1.5]

Manual Notch (if adaptive fails):
P08-30: _____ (Notch 1 freq, Hz)
P08-31: _____ (Notch 1 width)
P08-32: _____ (Notch 1 depth)

Baseline Configuration (Before Changes):
P01-02: 0 (Manual mode - CAUSING BUZZING)
P01-03: 13 (Medium-high rigidity - Contributing to buzzing)
P01-04: 2.50 (Inertia ratio - OK)

Performance Results:
- Buzzing eliminated: Y/N
- Position accuracy: ±_____ encoder counts
- Settling time: _____ ms
- Following error: _____ max
- System temperature: _____ °C
- Notes: _________________________________
```

## Safety Notes

1. **Always ensure proper safety systems** before tuning
2. **Start with conservative settings** and increase gradually
3. **Monitor servo temperature** during tuning
4. **Stop immediately** if unusual noise or vibration occurs
5. **Keep emergency stop accessible** at all times

## Summary

This systematic approach should eliminate servo buzzing while maintaining acceptable performance. The key is to:
1. Start with system identification (inertia)
2. Reduce gains systematically
3. Add appropriate filtering
4. Use vibration suppression features
5. Optimize gradually

Remember: Every mechanical system is different - use this as a starting point and adapt based on your specific application requirements.
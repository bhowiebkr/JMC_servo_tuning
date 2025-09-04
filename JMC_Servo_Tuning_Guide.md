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

## Quick Reference - Specific Fixes for Your System

**⚠️ CRITICAL: Based on your actual parameter analysis, the main buzzing cause is P02-13 = 29 (too high dynamic gain)**

**Immediate Actions for Your Buzzing (in order):**
1. **Enable adaptive notch detection:** P08-11 = 1 (run for 2-5 minutes during typical moves)
2. **Freeze the detected notch:** P08-11 = 0 (locks the found resonance frequency) 
3. **Add torque filtering:** P08-20 = 1.5ms (smooths torque commands)
4. **Reduce dynamic gain:** P02-13 from 29→24 (main buzzing fix for motion)
5. **Optional speed filtering:** P08-19 = 0.5-1.0ms (if high-freq hiss remains)

**Keep these current values (already optimized):**
- P02-10 = 20 (static gain already lowered appropriately)  
- P02-11 = 11ms (static integral already adjusted)
- P02-14 = 1000ms (dynamic integral disabled - this is correct)

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

## Detailed Analysis of Your Current Parameters

### Critical Speed Loop Settings (From Your JSON File)
**Current Speed Loop Gains:**
- **P02-10** (Speed proportional gain 1 / static Kp): **20.0** (↓ already lowered from default ~27)
- **P02-11** (Speed integral constant 1 / static Ki time): **11.0ms** (↑ already raised from default ~10ms)  
- **P02-13** (Speed proportional gain 2 / dynamic Kp): **29.0** (↑ **PROBLEM: raised above default ~27**)
- **P02-14** (Speed integral constant 2 / dynamic Ki time): **1000ms** (maxed out - effectively disables integral during motion)

### Filtering & Vibration Suppression Status
**Current Filter Settings:**
- **P08-11** (Adaptive notch filter mode): **0 → OFF** (No automatic resonance suppression)
- **P08-19** (Feedback speed LPF): Not set (assume default = 0ms / off)
- **P08-20** (Torque command filter): Not listed in JSON (likely factory ~0.8ms - minimal filtering)
- **P08-30...** (Manual notch parameters): Not set (no manual resonance suppression)

### Root Cause Analysis
**Why You're Experiencing Buzzing:**

1. **High Dynamic Gain (P02-13 = 29):** You've raised the dynamic speed gain above factory default, making the servo very stiff during motion. This easily excites structural resonances causing the buzzing during moves.

2. **No Filtering Active:** With adaptive notch disabled and minimal torque filtering, any mechanical resonance frequencies are amplified rather than suppressed.

3. **Imbalanced Gain Strategy:** You correctly lowered static gains (P02-10, raised P02-11) for smooth holding, but increased dynamic gain (P02-13) which works against buzz elimination.

4. **Disabled Dynamic Integral (P02-14 = 1000ms):** While this prevents integral windup, it means all dynamic control relies on proportional action, making the system more prone to oscillation.

**The Fix:** Your system needs dynamic gain reduction (P02-13: 29→24) combined with adaptive notch filtering, not automatic mode switching.

## Step-by-Step Buzzing Elimination Procedure

### Phase A: Adaptive Notch Detection & Filtering (Do These First)
**⚠️ SAFETY: Ensure servo is disabled before making parameter changes**

1. **Enable Adaptive Notch Detection:**
   ```
   Parameter: P08-11 (Adaptive notch filter mode)
   Current Value: 0 (OFF)
   New Value: 1 (Single adaptive notch active)
   Purpose: Let the servo automatically detect resonance frequencies
   ```

2. **Run Detection Routine:**
   - Enable servo and run through typical moves that cause buzzing
   - Continue for 2-5 minutes to allow full detection
   - Listen for reduction in buzzing as notch adapts
   - The servo will automatically find and suppress resonance frequencies

3. **Freeze the Detected Notch:**
   ```
   Parameter: P08-11
   Change Value: 1 → 0 (Freeze/lock the found notch settings)
   Purpose: Locks the automatically detected frequency so it won't drift
   Result: Notch filter remains active but stops adapting
   ```

4. **Add Torque Command Filtering:**
   ```
   Parameter: P08-20 (Torque command filter constant)
   Set Value: 1.5ms (start conservative)
   Effect: Smooths high-frequency torque commands that excite resonance
   ```

5. **Test Initial Results:**
   - Enable servo and test motion
   - If significant improvement, proceed to Phase B
   - If buzzing remains, continue with gain reduction

### Phase B: Dynamic Gain Reduction (Main Fix)

6. **Reduce Dynamic Speed Gain (CRITICAL FIX):**
   ```
   Parameter: P02-13 (Speed proportional gain 2 - Dynamic Kp)
   Current Value: 29.0 (TOO HIGH - main cause of buzzing)
   New Value: 24.0 (start here, can try 25.0 if too sluggish)
   Effect: Reduces dynamic stiffness that excites resonance during motion
   ```

7. **Test Motion Performance:**
   - Enable servo and run typical moves that previously caused buzzing
   - Check for buzzing elimination during acceleration/deceleration
   - Verify motion isn't too sluggish (if so, try 25.0 instead of 24.0)
   - Monitor positioning accuracy

8. **Optional: Add Speed Feedback Filtering (if needed):**
   ```
   Parameter: P08-19 (Speed feedback filter)
   Set Value: 0.5-1.0ms (only if high-frequency hiss remains)
   Effect: Filters speed feedback noise, but adds slight lag
   Warning: Start with 0.5ms, don't exceed 1.0ms to avoid sluggish response
   ```

9. **Test Complete System:**
   - Run full range of typical motions
   - Verify buzzing is eliminated throughout motion range
   - If stable, proceed to Phase C for optimization

### Phase C: Performance Optimization (After Buzzing Eliminated)

10. **Test for Performance vs. Stability Balance:**
    - With P02-13 = 24, test motion responsiveness
    - If motion feels sluggish and no buzzing, try P02-13 = 25
    - If 25 is stable, optionally test P02-13 = 26 (but monitor closely)
    - Stop at first sign of buzzing return

11. **Fine-tune Torque Filtering:**
    ```
    If system is stable with P08-20 = 1.5ms:
    - Try reducing to P08-20 = 1.0ms for faster response
    - Test thoroughly for buzzing return
    - If buzzing returns, revert to 1.5ms
    ```

12. **Final System Validation:**
    - Run servo through complete motion range
    - Test positioning accuracy and repeatability  
    - Monitor servo temperature during extended operation
    - Verify no unusual noise throughout travel
    - Document successful parameter set

## Manual vs. Automatic Mode Decision

### Option 1: Continue Manual Tuning (Recommended for Your Situation)
Since you've already invested time in manual tuning and have some gains optimized, you may want to continue in manual mode:

**Advantages:**
- Keep your existing optimized static gains (P02-10=20, P02-11=11ms)  
- Only need to fix the problematic dynamic gain (P02-13: 29→24)
- More precise control over individual parameters
- No risk of automatic mode overriding your good settings

**This Approach:** Focus on the specific fixes in Phase A-C above

### Option 2: Switch to Automatic Mode (Alternative)
If you want to start fresh with automatic tuning:

**Parameters to change:**
- P01-02: 0 → 1 (Enable standard automatic rigidity adjustment)
- P01-03: 13 → 8 (Conservative starting rigidity level)

**Advantages:**
- Automatic optimization for your 2.5:1 inertia ratio
- Built-in gain relationships and filtering
- Less manual tuning required

**Disadvantages:**  
- May override your already-good static gain settings
- Less granular control over individual parameters

## Exact Parameter Change Table (Copy-Paste Ready)

**Apply these changes in the specified order for optimal results:**

| Parameter | Description | Current Value | Recommended Value | Notes & Testing |
|-----------|-------------|---------------|-------------------|-----------------|
| **P08-11** | Adaptive notch filter mode | 0 (OFF) | **1** → run 2-5 minutes → **0** | Enable to detect resonance, then freeze. Run typical moves while P08-11=1 until tone reduces, then set to 0 to lock. |
| **P08-20** | Torque command filtering | ~0.8ms (default) | **1.5ms** | Smooths torque spikes that excite resonance. If still noisy, try 2.0-3.0ms. Small values retain responsiveness. |
| **P02-13** | Speed prop gain 2 (Dynamic Kp) | **29.0** | **24.0** (or 25.0) | **MAIN FIX** - Reduces dynamic stiffness causing motion buzzing. Try 25.0 if 24.0 feels sluggish. |
| **P02-10** | Speed prop gain 1 (Static Kp) | **20.0** | **Keep 20.0** | Already optimized. Only reduce to 16-18 if idle buzzing persists after notch/filter. |
| **P02-11** | Speed integral 1 (Static Ki time) | **11.0ms** | **Keep 11.0ms** | Already optimized. Could try 10.0ms for firmer hold if needed after reducing P02-13. |
| **P02-14** | Speed integral 2 (Dynamic Ki time) | **1000ms** | **Keep 1000ms** | Effectively disables dynamic integral - this is correct. Only change if following error issues. |
| **P08-19** | Speed feedback LPF | 0ms (off) | **Optional: 0.5-1.0ms** | Only if high-freq hiss remains after notch+torque filter. Adds lag - use sparingly. |

### Manual Notch (If Adaptive Fails)
| Parameter | Description | Set Only If Needed | Notes |
|-----------|-------------|-------------------|-------|
| **P08-30** | Manual notch 1 frequency | Monitor detected Hz | Set to frequency found during adaptive phase |
| **P08-31** | Manual notch 1 width | 2 | Width=2, depth=30-50 is good starting point |
| **P08-32** | Manual notch 1 depth | 30-50 | Lower values = deeper suppression |

### Step-by-Step Application Instructions:
1. **Backup current parameters**
2. **Set P08-11 = 1** → Run typical moves for 2-5 minutes → **Set P08-11 = 0**
3. **Set P08-20 = 1.5ms** → Test
4. **Set P02-13 = 24.0** → Test motion (try 25.0 if too sluggish)
5. **If still buzzing:** Increase P08-20 → 2.0ms, retest
6. **If particular frequency remains:** Set manual notch parameters
7. **Optional:** Add P08-19 = 0.5ms if faint hiss remains

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

### Issue: Buzzing from High Dynamic Gain (Your Current Configuration)
**Root Cause:** P02-13 = 29 (dynamic speed gain too high) + no filtering active

**Immediate Solutions (in order):**
1. **Enable adaptive notch:** P08-11 = 1 → run moves → P08-11 = 0 (Most effective first step)
2. **Add torque filtering:** P08-20 = 1.5ms (Smooths excitation)
3. **Reduce dynamic gain:** P02-13 = 29 → 24 (Main buzzing fix for motion)
4. **Optional speed filter:** P08-19 = 0.5-1.0ms (if hiss remains)

**Why This Happens:**
- P02-13 = 29 makes servo very stiff during motion, exciting structural resonances
- No filtering active (P08-11=0, minimal P08-20) allows resonances to build
- Static gains (P02-10, P02-11) already optimized, dynamic gain is the problem
- P02-14=1000ms disables dynamic integral, making system rely on proportional control

**Progressive Tuning After Fix:**
1. Test with P02-13 = 24 first (should eliminate buzzing)
2. If motion feels sluggish, try P02-13 = 25
3. If still stable and need more performance, try P02-13 = 26
4. Monitor for buzzing return at each step - stop immediately if it returns

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

Critical Tuning Parameters (Current Values from JSON Analysis):
P01-02: 0 (Manual mode - keeping in manual since gains partially optimized)
P01-03: 13 (Rigidity setting - keeping current since using manual gains)
P01-04: 2.50 (Load inertia ratio - Good)
P02-10: 20.0 (Speed prop gain 1) [KEEP - already optimized down from ~27]
P02-11: 11.0 (Speed integral 1, ms) [KEEP - already optimized up from ~10ms] 
P02-13: _____ (Speed prop gain 2) [CURRENT: 29.0 → CHANGE TO: 24.0-25.0]
P02-14: 1000 (Speed integral 2, ms) [KEEP - disables dynamic integral, correct]

Filtering & Vibration (Apply These Changes for Buzzing):
P08-11: _____ (Adaptive notch mode) [CURRENT: 0 → CHANGE: 1→0 freeze technique]
P08-19: _____ (Speed filter, ms) [CURRENT: 0 → ADD IF NEEDED: 0.5-1.0ms]
P08-20: _____ (Torque filter, ms) [CURRENT: ~0.8 → CHANGE TO: 1.5ms]

Manual Notch (if adaptive fails):
P08-30: _____ (Notch 1 freq, Hz) [Use frequency detected during adaptive phase]
P08-31: _____ (Notch 1 width) [Recommend: 2]
P08-32: _____ (Notch 1 depth) [Recommend: 30-50]

Baseline Configuration (Before Changes):
P01-02: 0 (Manual mode - can keep, some gains already optimized)
P01-03: 13 (Rigidity - not main issue)
P01-04: 2.50 (Inertia ratio - Good)
P02-13: 29.0 (MAIN PROBLEM - dynamic gain too high causing motion buzzing)
P08-11: 0 (No adaptive notch - missing critical resonance suppression)

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
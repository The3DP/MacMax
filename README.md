# MacMax
This is a CPU test made for any Mac. 
The testing is very simple and extremely easy.
All you need to do is copy the code, then 
paste it into your Mac's Terminal.

# Testing Levels

There are 5 different levels of CPU testing you can choose from:

Level 1: Light Test (Single-threaded math)

Level 2: Medium Test (Floating-point math)

Level 3: Heavy Load (Multi-core test using multiprocessing)

Level 4: Stress Test (Full CPU load with continuous loops)
⚠️ WARNING: This will max out all CPU cores indefinitely. You’ll need to stop it manually:
Press Ctrl+C or run:
killall Python

Level 5: Extreme Test (High CPU + memory pressure)
⚠️ DANGER: This will stress both CPU and memory heavily.
It may cause system slowdown or even crash on some Macs.
Monitor your system temperature and resource usage
(Activity Monitor or top).

🧯 Stop All Tests
To kill all Python scripts running in the background:

killall Python
killall python3

# Benchmark Options

Want to find out your CPU's real-time performance instead of just stressing it? 
If that's the case for you, then use the file "BenchTest.py" 

# Want to know more?

If you have any questions or comments about this repository, I'd like to hear from you! 
Just contact me at d73928430@gmail.com

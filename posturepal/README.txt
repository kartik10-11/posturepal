╔══════════════════════════════════════════════════════════╗
║     AI POSTURE CORRECTION SYSTEM — SETUP GUIDE          ║
║     For Complete Beginners — Follow Step by Step!       ║
╚══════════════════════════════════════════════════════════╝

YOUR PROJECT FOLDER STRUCTURE:
───────────────────────────────
posturepal/
├── app.py                  ← Flask backend (the server)
├── requirements.txt        ← Python libraries needed
├── posture_logs.json       ← Created automatically when app runs
├── README.txt              ← This file
└── templates/
    └── index.html          ← Frontend (the website)


══════════════════════════════════════════
STEP 1 — Install Python
══════════════════════════════════════════
1. Go to: python.org/downloads
2. Click "Download Python 3.11" (or latest)
3. Run the installer
4. IMPORTANT: Check the box "Add Python to PATH"
5. Click Install Now
6. Verify: open Command Prompt and type:
   python --version
   (should show Python 3.x.x)


══════════════════════════════════════════
STEP 2 — Open Command Prompt in Your Folder
══════════════════════════════════════════
1. Open File Explorer
2. Go to your posturepal folder
3. Click on the address bar at the top
4. Type:  cmd
5. Press Enter
6. A black command prompt window opens IN that folder


══════════════════════════════════════════
STEP 3 — Install Flask (One Time Only)
══════════════════════════════════════════
In the command prompt, type this and press Enter:

   pip install -r requirements.txt

Wait for it to finish. You will see "Successfully installed flask"


══════════════════════════════════════════
STEP 4 — Run the Server
══════════════════════════════════════════
In the command prompt, type:

   python app.py

You will see:
   ==================================================
     AI Posture Correction System - Backend
     Open browser at: http://localhost:5000
   ==================================================

Keep this window OPEN (do not close it!)


══════════════════════════════════════════
STEP 5 — Open the App
══════════════════════════════════════════
1. Open Google Chrome
2. Type in address bar:  http://localhost:5000
3. Press Enter
4. You will see the PosturePal AI app!
5. Click "Start Camera"
6. Allow camera access
7. The AI will start detecting your posture!


══════════════════════════════════════════
HOW THE APP WORKS
══════════════════════════════════════════

Frontend (index.html):
  - Your webcam streams video
  - MediaPipe AI library detects 33 body points
  - JavaScript calculates angles between body points
  - Classifies posture as Correct / Bad / Worst
  - Shows real-time suggestions

Backend (app.py / Flask):
  - Receives posture data from frontend via API
  - Stores data in posture_logs.json
  - Provides summary statistics
  - Serves the website at localhost:5000

API Endpoints:
  GET  /                    → Opens the website
  POST /api/log-posture     → Saves posture data
  GET  /api/get-logs        → Returns all logs
  GET  /api/summary         → Returns statistics
  POST /api/clear-logs      → Clears all logs


══════════════════════════════════════════
POSTURE CLASSIFICATION RULES
══════════════════════════════════════════

Neck Angle:
  < 20°   → ✅ Good
  20-35°  → ⚠️ Bad
  > 35°   → ❌ Worst

Spine Angle:
  < 15°   → ✅ Good
  15-30°  → ⚠️ Bad
  > 30°   → ❌ Worst

Shoulder Level Difference:
  < 5     → ✅ Good
  5-10    → ⚠️ Bad
  > 10    → ❌ Worst

Hip Alignment Difference:
  < 5     → ✅ Good
  5-10    → ⚠️ Bad
  > 10    → ❌ Worst

DECISION:
  2+ Worst flags → Worst Posture ❌
  1+ Bad flags   → Bad Posture ⚠️
  All good       → Correct Posture ✅


══════════════════════════════════════════
FOR DEPLOYMENT (Phase 3)
══════════════════════════════════════════
Option A: Vercel (Frontend only)
  1. Upload index.html to Vercel
  2. Get free public URL

Option B: PythonAnywhere (Full Stack)
  1. Go to pythonanywhere.com
  2. Upload your entire posturepal folder
  3. Set up Flask app
  4. Get free public URL like:
     yourname.pythonanywhere.com


══════════════════════════════════════════
TECH STACK SUMMARY 
══════════════════════════════════════════
Frontend:   HTML5, CSS3, JavaScript (Vanilla)
AI Model:   MediaPipe Pose (Google) — pre-trained
Detection:  Rule-based angle calculation
Backend:    Python Flask
Storage:    JSON file (simple database)
Deployment: Vercel / PythonAnywhere

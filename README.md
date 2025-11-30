# AgriAide — Multi-Agent Agricultural AI Assistant
<img width="1536" height="1024" alt="AGRIAIDE" src="https://github.com/user-attachments/assets/3c03374e-0c8d-4a59-8a9c-28cf90882ec0" />


**1. Problem Statement**

Smallholder farmers often struggle with:
- Identifying plant diseases early
- Lack of reliable crop advisory support
- Limited access to agriculture extension workers
- Difficulty finding affordable inputs or treatments
This leads to reduced crop yield, financial losses, and delayed disease management.

**2. Proposed Solution — AgriAide**

AgriAide is a multi-agent AI system that helps farmers diagnose plant leaf diseases and get personalised, actionable recommendations.

It consists of four coordinated agents:

Diagnosis Agent:

- Accepts an image of a plant leaf
- Performs disease classification
- Returns top diagnosis + confidence

Advisory Agent:

- Generates safe, low-cost, farmer-friendly solutions
- Provides actionable steps with dosage & safety

Marketplace Agent:

- Suggests local suppliers, remedies, fertilizers
- Uses a small synthetic marketplace DB (privacy-safe)

Memory Agent:

- Stores farmer preferences (crop type, language)
- Enables personalization and re-usage
- Fully opt-in + privacy-conscious

**3.Why This Project? (Impact)**

- Supports thousands of smallholder farmers who often have no expert support.
- Reduces dependency on expensive agronomists.
- Low-tech + mobile-friendly; can be Dockerized for easy deployment.
- Privacy-first: on-device storage & explicit opt-in for memory.
- Multilingual-ready for rural accessibility.

This aligns directly with the Agents for Good objectives.

**Essential Tools and Utilities in AgriAide**

The AgriAide system relies on a set of internal tools and utilities that enable its multi-agent workflow. These tools help each agent perform reliably, validate outputs, and maintain an iterative, quality-focused loop. The following components play a crucial role in delivering accurate diagnostics, tailored agricultural recommendations, and a smooth end-user experience.

Image Processing & Storage `save_image_to_disk`:

This utility ensures that every uploaded leaf image is safely stored in a managed directory, tagged with a unique ID. It allows the Diagnosis Agent to consistently access the correct image file and ensures reproducibility for judges and developers.

- Handles file creation and path generation
- Prevents name collisions using UUIDs
- Organizes uploaded images for auditing and evaluation
- This is fundamental for making the entire diagnosis pipeline deterministic and traceable.

Codebase Analysis `analyze_codebase`:

AgriAide includes a lightweight tool that analyzes the local repository to assist with debugging, validation, and automated documentation.

- Recursively scans the repository using glob and os
- Consolidates codebase context for internal reporting
- Handles UnicodeDecodeError by retrying with fallback encodings

This ensures that any agent responsible for reporting or content generation has accurate technical context, improving correctness in documentation and evaluation.

Disease Classification Helper `diagnosis_engine`:

Though the current demo uses a placeholder classifier, this module is structured to plug in any image-based disease model — Torch, ONNX, or an LLM-based vision API.

Key capabilities:
- Standardized input preprocessing
-Confidence scoring utilities
- Mappable disease identifiers for downstream Advisory Agent use
- This design keeps AgriAide modular and model-agnostic.

Advisory Knowledge Base Utility `advisory_lookup`:

The Advisory Agent uses a curated mini-knowledge base, stored locally as a dictionary or JSON file.

This tool:
- Maps disease IDs to safe, low-cost treatment options
- Ensures content is deterministic and not hallucinated
- Provides farmer-friendly phrasing and safety precautions
- Structured KB makes the system scientifically grounded instead of purely generative.

Marketplace Database Helper `supplier_search`:

This utility enables the Marketplace Agent to return contextually relevant local suppliers or agricultural inputs.

It includes:
- A synthetic privacy-safe local supplier index
- Fallback responses when no match is found
- Extensible schema for real-world integration later
-This allows AgriAide to simulate low-cost procurement suggestions without exposing personal data.

Validation Checkers (DiagnosisValidationChecker, AdvisoryValidationChecker):

AgriAide employs lightweight validation agents to ensure output quality at each step.

These validators:
- Check that a diagnosis is present and structurally valid
- Ensure advisory recommendations are non-empty and safe
- Escalate via a signal when validation succeeds (EventActions equivalent)
- Do nothing on failure — prompting the LoopAgent to retry

This creates a robust, iterative refinement loop and prevents incomplete or unsafe outputs from reaching the user.

Memory Manager (SQLite Memory Tool):

AgriAide includes a privacy-first memory layer using SQLite.
Responsibilities:
-Stores user preferences (language, crop type)
-Logs interactions for personalization
-Enables opt-in data retention
-Ensures on-device, offline-first privacy

This gives the system the ability to “remember” farmers in a controlled, user-friendly way.

## Features
- Multi-agent architecture
- Leaf disease diagnosis
- Personalized advisory
- Local supplier recommendations
- SQLite memory
- Flask UI
- Docker support

## Run Locally
pip install -r requirements.txt

python app.py
 ## Docker Deployment
docker build -t agriaide .

docker run -p 7860:7860 agriaide

**Value Statement**

AgriAide saves farmers valuable time by quickly diagnosing plant diseases and providing clear, actionable advice. It reduces guesswork, improves decision-making, and helps farmers protect their crops more efficiently.
If I had more time, I would add an agent that continuously scans agricultural news, regional pest alerts, and weather-driven disease forecasts. Integrating such a research-focused agent would help anticipate emerging threats and proactively recommend preventive measures. This requires combining external APIs, agricultural data portals, or custom-built retrieval tools.

"""Structured resume data for the portfolio website."""

PROFILE = {
    "name": "Ayman Sayed",
    "title": "AI & ML Developer",
    "tagline": (
        "Building intelligent systems at the intersection "
        "of software engineering and machine learning"
    ),
    "phone": "+1 (346) 871 8119",
    "email": "aym_s@outlook.com",
    "website": "https://aymanai.com",
    "linkedin": "https://www.linkedin.com/in/ayman-sayed-b8ba80176/",
    "github": "https://github.com/ayman-tech",
    "location": "Washington DC, USA",
}

EDUCATION = [
    {
        "degree": "Master's in Applied Machine Learning",
        "school": "University of Maryland, College Park",
        "period": "Expected 2027",
        "courses": [
            "Principles of ML",
            "Computing Systems for ML",
            "Principles of Data Science",
            ""
        ],
    },
    {
        "degree": "Bachelor's in Computer Science",
        "school": "National Institute of Technology, Rourkela",
        "period": "2019 - 2023",
        "courses": [
            "Data Structures & Algorithms",
            "OS",
            "Computer Architecture",
            "Cloud Computing",
            "Machine Learning",
            "Artificial Intelligence",
        ],
    },
]

EXPERIENCE = [
    {
        "company": "University of Maryland, College Park",
        "role": "Graduate Research Assistant, PARETO Group",
        "location": "College Park, MD, USA",
        "period": "Dec 2025 \u2013 Present",
        "bullets": [
            "Developed & trained a Reinforcement Learning agent on the XRO climate model to induce sustained ENSO events by controlling 9 coupled ocean–atmosphere modes with physics-based dynamics; discovered critical preconditions for multi-year El Niño/La Niña events through learned policy analysis.",
            "Awarded NASA funding to build a conditional diffusion-based super-resolution pipeline that downscales coarse 2 km GOES satellite imagery to 30 m spatial resolution, enabling high-fidelity urban heat island analysis.",
            "Extended DeepMind's GenCast diffusion model with gradient-based guidance for controllable tropical cyclone trajectory forecasting over 4-day horizons; designed a parallel ReadOut GNN decoder for binary storm classification from diffusion latents with dynamic class weighting for <1% positive class ratio.",
            "Implemented inner latent optimization within DPM-Solver++ sampling using gradient clipping, selective spatial masking, and local affine warping for stable multi-step guided generation; built an ERA5-to-storm-mask data pipeline processing 0.25° global reanalysis data with variable-radius cyclone annotations.",
        ],
    },
    {
        "company": "Samsung Research Institute Bangalore",
        "role": "Senior Software Developer, Platform Intelligence",
        "location": "Bangalore, KA, India",
        "period": "Feb \u2013 Aug 2025",
        "bullets": [
            "Fine tuned Gauss AI model using QLoRA to detect unauthorized access and potential threat environments during interactions with sensitive applications.",
            "Built Agentic AI workflow for SEAL (Smart Efficient App Lock) model to identify unauthorized access to device.",
            "Developed out-of-box on-boarding service that seamlessly sync WiFi profiles and Samsung accounts on PC from Android devices during first-time PC startup.",
            "Integrated Knox Matrix (KM) Windows on Samsung Cloud, Internet, and Notes for seamless end-to-end encrypted sync of data between Android and Windows devices.",
        ],
    },
    {
        "company": "Samsung Research Institute Bangalore",
        "role": "Software Developer, On Device AI",
        "location": "Bangalore, KA, India",
        "period": "Nov 2023 \u2013 Feb 2025",
        "bullets": [
            "Developed Key Provisioning system providing hardware backed root of trust on Samsung PC\u2019s and successfully commercialized it with 2 Million+ active users.",
            "Engineered security validation of TPM, Secure Boot, Kernel DMA protection & Memory Integrity for Knox suite of Windows Security.",
            "Implemented REST handlers to facilitate server connections for Knox Matrix; improved code quality & stability, achieving 35% performance increase.",
            "Built framework linking Trustchain service with Big Data server to stream event data & enable crash reporting.",
        ],
    },
    {
        "company": "Samsung Research Institute Bangalore",
        "role": "SDE Intern, Visual Intelligence",
        "location": "Bangalore, KA, India",
        "period": "May \u2013 Jul 2022",
        "bullets": [
            "Developed app to analyze capabilities of multiple cameras of connected mobile devices.",
            "Built a Flask dashboard that allows operations such as search by ID or any of 400 properties, display vendor tags, compare cameras across devices.",
        ],
    },
]

PROJECTS = [
    {
        "name": "Triage AI",
        "tech": ["Python", "LangGraph", "OpenAI", "PostGres Vector", "ElevenLabs", "Twilio", "FastAPI", "PostGres SQL", "Jinja2", "Tesseract", "Docker", "Langsmith"],
        "description": "Multi-agent AI system for automated Complaint Management using a supervisor-orchestrated Agentic workflow with specialist agents for classification, risk assessment, root cause analysis, and resolution. Integrated RAG with pgvector, OCR document processing, voice intake via Twilio + ElevenLabs , and a dual evaluation framework with LLM-as-judge and benchmark datasets.",
        "icon": "support_agent",
        "status": "Live", # if live will show green gif
        "product_link": "https://triage.aymanai.com",
        "link": "https://github.com/ayman-tech/Multi-Agent-Complaint-System",
    },
    {
        "name": "DeepRAG",
        "tech": ["Python", "RAG", "BGE-M3", "Qdrant", "DeepSeek", "FastAPI", "NiceGUI"],
        "description": "Engineered end-to-end RAG pipeline with hybrid dense/sparse retrieval, Qdrant vector indexing, cross-encoder reranking, and DeepSeek chain-of-thought generation, served via FastAPI+NiceGUI.",
        "icon": "psychology",
        "status": "Live",
        "product_link": "https://deeprag.aymanai.com",
        "link": "https://github.com/ayman-tech/deep-rag",
    },
    {
        "name": "Chart VLM",
        "tech": ["Python", "PyTorch", "Quantization", "VLM", "LoRA", "HuggingFace"],
        "description": "Developed & fine-tuned Vision Language Model (Qwen2-VL) using PEFT & Hugging Face TRL library on ChartQA dataset to answer questions based on images of charts, enabling automated data analysis.",
        "icon": "bar_chart",
        "status": "Pre-Deployment",
        "product_link": None,
        "link": None,
    },
    {
        "name": "ENSO Prediction using RL",
        "tech": ["Python", "Gymnasium", "Stable-Baselines-3", "PPO", "XRO Model"],
        "description": "Research project under Dr. Maria Molina, designing & training a Reinforcement Learning agent with Stable-Baselines3 & XRO model to induce multi-year ENSO events, increasing control efficacy by 48%.",
        "icon": "waves",
        "status": "Pre-Deployment",
        "product_link": "https://github.com/ayman-tech/enso-rl",
        "link": "https://github.com/ayman-tech/enso-rl",
    },
    {
        "name": "Optimal Transport Knowledge Distillation",
        "tech": ["LangGraph", "Python", "Groq", "StateGraph", "ReactAgent", "LangChain tools", "LangSmith"],
        "description": "Developed a knowledge distillation framework using Sinkhorn Optimal Transport with a jointly optimized learnable cost matrix to efficiently compress vision models while preserving semantic class relationships.",
        "icon": "code",
        "status": "Pre-Deployment",
        "product_link": "https://github.com/ayman-tech/sinkhorn-vision-kd",
        "link": "https://github.com/ayman-tech/sinkhorn-vision-kd",
    },
    {
        "name": "Tap Code",
        "tech": ["LangGraph", "Python", "Groq", "StateGraph", "ReactAgent", "LangChain tools", "LangSmith"],
        "description": "Agentic AI system that generates full-stack application code from input prompt.",
        "icon": "code",
        "status": "Pre-Deployment",
        "product_link": "https://github.com/ayman-tech/tapcode",
        "link": "https://github.com/ayman-tech/tapcode",
    },
    {
        "name": "Potato Disease Analyzer",
        "tech": ["Python", "TensorFlow", "Keras", "CNN", "FastAPI", "Android", "GCP"],
        "description": "Website & Android app that identifies & classifies disease in potato plants by analyzing images of leaves using CNN-based deep learning models.",
        "icon": "eco",
        "status": "Pre-Deployment",
        "product_link": "https://github.com/ayman-tech/potato-disease-analyzer",
        "link": "https://github.com/ayman-tech/potato-disease-analyzer",
    },
]

SKILLS = {
    "Programming": {
        "icon": "code",
        "items": ["C", "C++", "Python", "C#", "Java", "HTML", "CSS", "JavaScript", "Bash", "Dart"],
    },
    "App Frameworks": {
        "icon": "web",
        "items": ["UWP", ".NET", "Android Studio", "WPF", "Bootstrap", "NodeJS", "React"],
    },
    "Data Stack": {
        "icon": "storage",
        "items": ["Tableau", "SQL", "MongoDB", "NumPy", "Pandas", "MatPlotLib", "Plotly"],
    },
    "Machine Learning": {
        "icon": "psychology",
        "items": ["TensorFlow", "PyTorch", "Keras", "LangChain", "LangGraph", "LLM", "RAG", "NLP", "CV"],
    },
    "Technologies": {
        "icon": "build",
        "items": ["Git", "Docker", "Jenkins", "Jira", "REST APIs", "Linux"],
    },
}

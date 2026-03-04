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
    "linkedin": "https://linkedin.com/in/aymansayed",
    "github": "https://github.com/aymansayed",
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
        "name": "Chart VLM",
        "tech": ["Python", "PyTorch", "Quantization", "VLM", "LoRA", "HuggingFace"],
        "description": "Developed & fine-tuned Vision Language Model (Qwen2-VL) using PEFT & Hugging Face TRL library on ChartQA dataset to answer questions based on images of charts, enabling automated data analysis.",
        "icon": "bar_chart",
        "link": None,
    },
    {
        "name": "ENSO Prediction using RL",
        "tech": ["Python", "Gymnasium", "Stable-Baselines-3", "PPO", "XRO Model"],
        "description": "Research project under Dr. Maria Molina, designing & training a Reinforcement Learning agent with Stable-Baselines3 & XRO model to induce multi-year ENSO events, increasing control efficacy by 48%.",
        "icon": "waves",
        "link": "https://github.com",
    },
    {
        "name": "DeepRAG",
        "tech": ["Python", "RAG", "BGE-M3", "Qdrant", "DeepSeek", "FastAPI", "NiceGUI"],
        "description": "Engineered end-to-end RAG pipeline with hybrid dense/sparse retrieval, Qdrant vector indexing, cross-encoder reranking, and DeepSeek chain-of-thought generation, served via FastAPI+NiceGUI.",
        "icon": "psychology",
        "link": "https://github.com",
    },
    {
        "name": "Potato Disease Analyzer",
        "tech": ["Python", "TensorFlow", "Keras", "CNN", "FastAPI", "Android", "GCP"],
        "description": "Website & Android app that identifies & classifies disease in potato plants by analyzing images of leaves using CNN-based deep learning models.",
        "icon": "eco",
        "link": "https://github.com",
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

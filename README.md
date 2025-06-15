# Insurance-risk-analysis
Analysis historical insurance claim data to help optimize the marketing strategy as well as discover “low-risk” targets for which the premium could be reduced, hence an opportunity to attract new clients. 

# Task 2 – Data Version Control (DVC) Setup

For Task 2, I set up **Data Version Control (DVC)** to ensure all data used in my insurance analysis pipeline is reproducible, versioned, and auditable — a standard practice in regulated domains like finance and insurance.

---

## 🧱 Step-by-Step Setup

### ✅ 1. Created Task Branch
Merged Task 1 into `main`, then created a new branch:
```bash
git checkout main
git merge task-1
git checkout -b task-2
```

### ✅ 2. Installed and Initialized DVC

```bash
pip install dvc
dvc init
git add .dvc .dvcignore
git commit -m "Initialize DVC"
```

### ✅ 3. Configured Local Remote
```bash
mkdir /path/to/local/dvc-storage
dvc remote add -d localstorage /path/to/local/dvc-storage
```

### ✅ 4. Tracked My Cleaned Data

- I made sure .gitignore excludes the data/ folder but allows .dvc files.
- Then I added my cleaned data to DVC:
```bash
dvc add data/cleaned_claim_data.db
git add data/cleaned_claim_data.db.dvc .gitignore
git commit -m "Track cleaned data with DVC"
```

### ✅ 5. Pushed Data to Remote
```bash
dvc push
```

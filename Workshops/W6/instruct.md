

## Workshop 6

## Workshop Name: Validation, Verification, and CI with GitHub Action

## Description 

We will discuss validation, verification, and CI in the context of legal text understanding CFR document same as Assignment 5.

## Targeted Courses 

Software Quality Assurance 

## Activities 

### Pre-lab Content Dissemination 

**1. Validation:** Ensures the software meets customer requirements (i.e., “Are we building the right product?”). 

**2. Verification.** Ensures the software is built correctly according to specifications and design (i.e., “Are we building the product right?”).

**3. CI.** Software development practice where code changes are frequently merged into a shared repository and automatically built and tested to detect issues early.

We will use GitHub Actions to implement CI, catching issues early and maintaining code quality.



### In-class Hands-on Experience 
- Demo will be recorded and shared on CANVAS (Zoom Recordings).
- Go to [this repo](https://github.com/effat/GitHubActionSQA)
- File Descriptions
    - `raw_regulations.txt`: Raw input of CFR or user requirements
    -  `requirements.json` : Transformed raw input into user requirements for SDLC. This file will
                             be used in validation and verification step to ensure user requirements.
    -  `test_cases.json`:    Test cases for verfication to ensure the software meets requirements.
    -  `expected_structure.json`: Used in validation step to ensure the software meets requirements.

    - `scripts\verfification.py` : Verfification script
    - `scripts\validation.py`    : Validation script
    - `.github/workflows/github-actions-SQAdemo.yml` : GitHub Actions workflow file for automating CI.
        More on GitHub action: [GitHub Actions Quickstart](https://docs.github.com/en/actions/get-started/quickstart)

### Assignment 6 (Post Lab Experience) 
- Create a new public repo. Download all codes and use as template code.
- Comment Run Validation step in .yml file, update `test_cases.json` for B and C, and push
-  Take screen shots of example build 
- Update `requirements.json`, comment out Run Validation step in `.yml` file and push
- Take screen shots of example build
- Deadline: April 5, 2026

### Rubric
- Add test cases for B and C , run verification code [15%]
- Update `requirements.json` and Run Validation [15%]
- Examples of build failures [25%]
- Examples of build successes [25%]
- Your analysis of build failure and how you solved it to pass in CI [20%]


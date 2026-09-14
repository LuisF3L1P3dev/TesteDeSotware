# System Verification Test Plan for Advanced Color Module
**Revision:** 2.0  
**Date:** 2/22/00  
**Author:** Neil Bitzenhofer (Test/Tools Group)  
**System:** DataCard Series 9000 Card Personalization System  

---

## Table of Contents
1. Objectives of the Test
2. Test Description
   - 2.1 Description
   - 2.2 References
3. Schedule
4. Resources Required
5. Dependencies
6. Entry Criteria
7. Exit Criteria
8. Test Tools
9. Owner
10. Metrics
11. Test Plan Requirements Matrix
12. Document History
13. Definitions and Acronyms
- Appendix A: Test Plan Requirements Matrix
- Appendix B: Test Cases (B.1 Configuration/Install, B.2 Entrance, B.3 Main, B.4 Regression, B.5 Procedures)

---

## 1. Objectives of the Test
This document describes the test plan for the 9000 Advanced Color Module and includes information on what is to be tested, and how the testing is to be accomplished (test methodology). Specifically, this document describes the tests to be performed, the testing schedule, resources required, entry criteria, exit criteria, dependencies, test tools, metrics and the Test Plan Requirements Matrix. This is a living test plan and must be changed to reflect Core Team needs and requirements as they arise.

The main purpose of this test is to verify the requirements for the 9000 Advanced Color Module as set forth in SRS references.

---

## 2. Test Description

### 2.1 Description
Much of the functionality that was handled by the module firmware and DLL has been relegated to the Common Image Generator (CIG), and much of what is in the CIG is being tested by the UltraGraphics Module tests. System Verification Test (SVT) will be broken into three phases:
- **Entrance Testing:** Verify that the new Advanced Color Module can process a standard set of color images using 4 hybrids of Version A and B headers (72 test cases).
- **Main Test:** Thoroughly verify the operation of the Advanced Color Module software and hardware against SRS requirements (508 test cases).
- **Regression Test:** Performed as a subset of Main Test to verify product integrity after fixing Severity 1 and 2 defects (132 test cases).

### 2.2 References
1. Software Development Process Handbook (PEAQ)
2. Software Requirements Specification for the Advanced Color Module (May 13, 1999)
3. Software Requirements Specification for the Common Image Generator (May 28, 1999)
4. Structured Software Test Planning at DataCard (Benchmark Laboratories Inc., August 1996)

---

## 3. Schedule

| Test Sequence | Planned Start | Planned Finish | Actual Start | Actual Finish |
| :--- | :---: | :---: | :---: | :---: |
| 1. Test Development | 7-6-99 | 9-21-99 | 7-6-99 | 12-17-99 |
| 2. Module Availability | 9-20-99 | --- | --- | --- |
| 3. SVT Entrance Testing | 9-22-99 | 9-28-99 | 1-10-00 | 1-14-00 |
| 4. SVT Main Testing | 9-29-99 | 10-26-99 | 1-17-00 | 2-22-00 |
| 5. SVT Regression Testing | 10-27-99 | 11-2-99 | 2-15-00 | 3-15-00 |

---

## 4. Resources Required
- High Speed Advanced Color Module
- Standard Speed Advanced Color Module
- 9000 System dedicated to Advanced Color Module testing
- Latest CIG DLL and Advanced Color DLL
- Fully-loaded 9000 for Endurance and Performance testing
- Two SVT test personnel (minimum 80% time commitment)
- Consumables: 1 Tonal/Black ribbon, 5 Color ribbons, 1 case (4000) White MagStripe blank cards

---

## 5. Dependencies
- Advanced Color Module available and installed in lab 9000
- Common Image Generator (CIG) DLL available and loaded on 9000 Controller
- CIG Entrance Test executed
- UltraGraphics SVT executed in good portion
- Image and Module Profiles created and available

---

## 6. Entry Criteria
Satisfy all entry criteria defined in PEAQ Reference 1, plus completion of sufficient UltraGraphics SVT test cases.

---

## 7. Exit Criteria
Satisfy all exit criteria defined in PEAQ Reference 1.

---

## 8. Test Tools
- PVCS Tracker (Defect control reporting and tracking software)
- Hardware monitors

---

## 9. Owner
Test/Tools Group.

---

## 10. Metrics
Status and progress recorded through test case metrics (Appendix B). Defect, effort, and size metrics collected across testing phases.

---

## Appendix A: Test Plan Requirements Matrix

| Req # | Requirement Name | SRS Section | Notes / Test Cases |
| :---: | :--- | :---: | :--- |
| **1-A** | SSC-VerX Module Emulation File | 3.3.1 | ACM-05-3 through -12 |
| **1-B** | HSC Module Emulation File | 3.3.1 | ACM-05-2 |
| **1-C** | AC Module Emulation File | 3.3.2, 3.3.3 | ACM-05-1 and -3 |
| **2-A** | Color specification (Command CST) | 3.4.1.1 | ACM-01-108 |
| **2-B** | Horizontal and Vertical scaling | 3.4.1.4 | ACM-01-82, -83, -92, -93, -102, -103 |
| **2-C** | Background Color specification | 3.4.1.5 | ACM-01-114, -118, -122; ACM-03-193 |
| **2-D** | Foreground Color specification | 3.4.1.6 | ACM-01-115, -119, -123; ACM-03-193 |
| **2-E** | Opacity | 3.4.1.7 | ACM-01-85, -86; ACM-03-182, -184 |
| **2-F** | Z-order | 3.4.1.8 | ACM-01-87, -97; ACM-03-183, -184 |
| **2-G** | Image Color Profile | 3.4.1.9 | ACM-01-113, -117, -121 |
| **2-H** | Color Filter specification | 3.4.1.10 | ACM-01-112, -116, -120 |
| **3-A** | Overrides | 3.5 | ACM-03-19 through -180 |
| **4-A** | Version A, embedded | 3.6 | ACM-01-31 through -45 |
| **4-B** | Version A, file name | 3.6 | ACM-01-1 through -30 |
| **4-C** | Version B, embedded | 3.6 | ACM-01-62 through -77 |
| **4-D** | Version B, file name | 3.6 | ACM-01-46 through -61 |
| **5-A** | Increased number of shades | 3.8.1 | ACM-02-1 through -14 |
| **5-B** | Reduced tiling | 3.8.2 | ACM-02-15 and -16 |
| **8-A..I** | File Types (DPG, DPC, DIB, GIF, JPEG, TIF, TGA, BMP, PCX) | 3.11 | ACM-03 Series |
| **11-A** | Consistent error handling | 3.18.7 | ACM-04 |
| **12-A** | Performance requirements | 4 | ACM-06-6 through -9 |

---

## Appendix B: Test Case Overview
- **B.1 Installation Tests:** ACM-06-15 to ACM-06-21
- **B.2 Entrance Test:** `acmentr.doc` (72 test cases)
- **B.3 Main Test:** `acmsvt.doc` (508 test cases)
- **B.4 Regression Test:** `acmreg.doc` (132 test cases)
- **B.5 Test Case Procedures:** `ACM-01.DOC` to `ACM-06.DOC`

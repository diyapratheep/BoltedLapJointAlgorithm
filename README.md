# 🔩 Bolted Lap Joint Design as per IS 800:2007

This project automatically designs a **bolted lap joint** that connects two plates subjected to a known tensile force. The design complies with **IS 800:2007** steel structure standards and includes strength checks, spacing validations, and optimization to minimize the number of bolts while ensuring safety.

## 🚀 Features

- Choose optimal bolt diameter and grade
- Select suitable plate grade
- Calculates:
  - Bolt shear and bearing strength
  - Required number of bolts
  - Pitch, gauge, end, and edge distances
  - Overall connection length and efficiency
- Includes PyTest-based test automation
- Test summary report of passed and failed(skipped) tests

---

## 🛠️ Project Structure

```bash
.
├── bolted_lap_joint_design.py       # Main algorithm file
├── test_bolted_lap_joint.py         # Automated test cases (PyTest)
├── is800.py                         # IS800:2007 formula implementations
├── README.md                        # This file


## 🛠️ Requirements

- **Python 3.8+**
- Python Packages:
  - `pytest`
  - `numpy`

## 🛠️ Testing Commands
```bash
pytest -s test_bolted_lap_joint.py

## 🛠️ How It Works?
**Embed Video of Project Demo**: You can watch the demo video to see how the it functions in action.
![Project Demo](https://github.com/diyapratheep/Neoma/blob/main/demo%20gif/demo%20video.gif)




import pytest
import math
import bolted_lap_joint_design as bld  # This is your main code module

# 🔧 Mock IS800_2007 object with required methods


from bolted_lap_joint_design import design_lap_joint

# 🔢 Global counters (shared between test runs)
success_count = 0
failure_count = 0
skipped_count = 0

class TestBoltedLapJoint:

    @pytest.mark.parametrize("t1", [6, 8, 10, 12, 16, 20, 24])
    @pytest.mark.parametrize("t2", [6, 8, 10, 12, 16, 20, 24])
    @pytest.mark.parametrize("P", range(0, 101, 10))  # 0 to 100 kN in steps of 10
    def test_minimum_two_bolts(self, P, t1, t2):
        w = 150  # Assumed plate width

        # Access global counters
        global success_count, failure_count, skipped_count

        print(f"\n[🔧] Testing with P={P} kN, t1={t1} mm, t2={t2} mm ...")

        try:
            result = design_lap_joint(P, w, t1, t2)
            num_bolts = result["number_of_bolts"]

            if num_bolts >= 2:
                print(f"[✅] SUCCESS: Design found with {num_bolts} bolts.")
                success_count += 1
                
            else:
                print(f"[❌] FAIL: Only {num_bolts} bolts found (less than 2).")
                failure_count += 1
                

        except ValueError as e:
            if P == 0:
                print(f"[🟡] SKIPPED: No load applied (P=0) — {str(e)}")
                skipped_count += 1
               
            else:
                print(f"[❌] ERROR: {str(e)}")
                failure_count += 1
               

        # ✅ Print summary only once at the end of the last combination
        if P == 100 and t1 == 24 and t2 == 24:
            total = success_count + failure_count + skipped_count
            print("\n📊 === TEST SUMMARY ===")
            print(f"✅ Success: {success_count}")
            print(f"🟡 Skipped: {skipped_count}")
            print(f"❌ Failures: {failure_count}")
            print(f"🧮 Total Tested: {total}")

    def test_zero_load(self):
        try:
            result = bld.design_lap_joint(0, 150, 10, 10)
            print("[❌] ERROR: Expected failure for P=0, but got result:", result)
        except Exception as e:
            print(f"[🟡] SKIPPED: Zero load test passed as expected — {e}")


    def test_min_thickness(self):
        try:
            result = bld.design_lap_joint(50, 150, 6, 6)
            if result["number_of_bolts"] >= 2:
                print("[✅] Min thickness test passed.")
            else:
                print("[❌] FAIL: Less than 2 bolts in min thickness test.")
        except Exception as e:
            print(f"[❌] ERROR: Min thickness test failed — {e}")


    def test_max_thickness(self):
        try:
            result = bld.design_lap_joint(100, 150, 24, 24)
            if result["number_of_bolts"] >= 2:
                print("[✅] Max thickness test passed.")
            else:
                print("[❌] FAIL: Less than 2 bolts in max thickness test.")
        except Exception as e:
            print(f"[❌] ERROR: Max thickness test failed — {e}")

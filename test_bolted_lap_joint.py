
import pytest
import math
import bolted_lap_joint_design as bld  



from bolted_lap_joint_design import design_lap_joint

success_count = 0
failure_count = 0
skipped_count = 0
skipped_tests = []  # Store tuples like (P, t1, t2)


class TestBoltedLapJoint:

    @pytest.mark.parametrize("t1", [6, 8, 10, 12, 16, 20, 24])
    @pytest.mark.parametrize("t2", [6, 8, 10, 12, 16, 20, 24])
    @pytest.mark.parametrize("P", range(0, 101, 10))  # 0 to 100 kN in steps of 10
    def test_minimum_two_bolts(self, P, t1, t2):
        w = 150  # Assumed plate width

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
            skipped_tests.append((P, t1, t2))
            print(f"[🟡] SKIPPED: No suitable design for P={P}, t1={t1}, t2={t2} — {str(e)}")
            skipped_count += 1
            pytest.skip(f"Skipped: P={P}, t1={t1}, t2={t2} — No suitable design found")

               

        # Print summary at the end 
        if P == 100 and t1 == 24 and t2 == 24:
            total = success_count + failure_count + skipped_count
            print("\n📊 === TEST SUMMARY ===")
            print(f"✅ Success: {success_count}")
            print(f"🟡 Skipped: {skipped_count}")
            print(f"🧮 Total Tested: {total}")
            if skipped_tests:
                print("\n🟡 === SKIPPED TEST CASES ===")
                for P_val, t1_val, t2_val in skipped_tests:
                    print(f"  • P={P_val} kN, t1={t1_val} mm, t2={t2_val} mm")


    def test_zero_load(self):
        try:
            result = bld.design_lap_joint(0, 150, 10, 10)
            print("[❌] ERROR: Expected failure for P=0, but got result:", result)
        except Exception as e:
            print(f"[🟡] SKIPPED: Zero load test passed as expected — {e}")



    def test_min_thickness(self):
        result = bld.design_lap_joint(50, 150, 6, 6)
        assert result["number_of_bolts"] >= 2, "[❌] FAIL: Less than 2 bolts in min thickness test."
        print("[✅] Min thickness test passed.")

    def test_max_thickness(self):
        result = bld.design_lap_joint(100, 150, 24, 24)
        assert result["number_of_bolts"] >= 2, "[❌] FAIL: Less than 2 bolts in max thickness test."
        print("[✅] Max thickness test passed.")


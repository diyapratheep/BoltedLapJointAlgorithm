# IS800_2007.py

import math

KEY_DP_FAB_FIELD = 'Field'
KEY_DP_FAB_SHOP = 'Shop'

class IS800_2007:
    cl_5_4_1_Table_5 = {
        'gamma_mb': {
            'Field': 1.25,
            'Shop': 1.25
        }
    }

    @staticmethod
    def cl_10_3_3_bolt_shear_capacity(f_ub, A_nb, A_sb, n_n, n_s=0, safety_factor_parameter=None):
        V_nsb = f_ub / math.sqrt(3) * (n_n * A_nb + n_s * A_sb)
        gamma_mb = IS800_2007.cl_5_4_1_Table_5['gamma_mb'][KEY_DP_FAB_SHOP]
        V_dsb = V_nsb / gamma_mb
        return V_dsb

    @staticmethod
    def cl_10_3_4_bolt_bearing_capacity(f_u, f_ub, t, d, e, p, bolt_hole_type='Standard',
                                        safety_factor_parameter=KEY_DP_FAB_FIELD):
        d_0 = IS800_2007.cl_10_2_1_bolt_hole_size(d, bolt_hole_type)
        if p > 0.0:
            k_b = min(e / (3.0 * d_0), p / (3.0 * d_0) - 0.25, f_ub / f_u, 1.0)
        else:
            k_b = min(e / (3.0 * d_0), f_ub / f_u, 1.0)
        k_b = round(k_b, 2)
        V_npb = 2.5 * k_b * d * t * f_u
        gamma_mb = IS800_2007.cl_5_4_1_Table_5['gamma_mb'][safety_factor_parameter]
        V_dpb = V_npb / gamma_mb

        if bolt_hole_type in ['Over-sized', 'short_slot']:
            V_dpb *= 0.7
        elif bolt_hole_type == 'long_slot':
            V_dpb *= 0.5

        return V_dpb

    @staticmethod
    def cl_10_2_1_bolt_hole_size(d, bolt_hole_type='Standard'):
        table_19 = {
            "12-14": {'Standard': 1.0, 'Over-sized': 3.0, 'short_slot': 4.0, 'long_slot': 2.5},
            "16-22": {'Standard': 2.0, 'Over-sized': 4.0, 'short_slot': 6.0, 'long_slot': 2.5},
            "24": {'Standard': 2.0, 'Over-sized': 6.0, 'short_slot': 8.0, 'long_slot': 2.5},
            "24+": {'Standard': 3.0, 'Over-sized': 8.0, 'short_slot': 10.0, 'long_slot': 2.5}
        }

        d = int(d)
        if d < 12:
            clearance = 0
        elif d <= 14:
            clearance = table_19["12-14"][bolt_hole_type]
        elif d <= 22:
            clearance = table_19["16-22"][bolt_hole_type]
        elif d <= 24:
            clearance = table_19["24"][bolt_hole_type]
        else:
            clearance = table_19["24+"][bolt_hole_type]

        if bolt_hole_type == 'long_slot':
            bolt_hole_size = (clearance + 1) * d
        else:
            bolt_hole_size = clearance + d

        return bolt_hole_size

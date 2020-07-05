def slam(data, N, num_landmarks, world_size, motion_noise, measurement_noise):
    
    cons_omega, cons_xi = initialize_constraints(N, num_landmarks, world_size)
    
    for idx, item in enumerate(data):
        meas = item[0]
        mot = item[1]
        
        pdb.set_trace()
        dat_idx = 2*idx
        # prev step flipx
        cons_omega[dat_idx][dat_idx] += 1
        cons_omega[dat_idx][dat_idx + 2] -= 1
        cons_xi[dat_idx][0] -= mot[0]
        
        # prev step flipy
        cons_omega[dat_idx + 1][dat_idx + 1] += 1
        cons_omega[dat_idx + 1][dat_idx + 3] -= 1
        cons_xi[dat_idx + 1][0] -= mot[1]
        
        
        # next step flipx
        cons_omega[dat_idx + 2][dat_idx] -= 1
        cons_omega[dat_idx + 2][dat_idx + 2] += 1
        cons_xi[dat_idx + 2][0] += mot[0]
        
        # next step flipy
        cons_omega[dat_idx + 3][dat_idx + 1] -= 1
        cons_omega[dat_idx + 3][dat_idx + 3] += 1
        cons_xi[dat_idx + 3][0] += mot[1]
        
        # landmarks flipx
        for i in range(len(meas)):
            
            land_grid_num = (N + meas[i][0])*2
            
            # state flipx
            cons_omega[dat_idx][dat_idx] += 1
            cons_omega[dat_idx][land_grid_num] -= 1
            cons_xi[dat_idx][0] -= meas[i][1]
        
            # state flipy
            cons_omega[dat_idx + 1][dat_idx + 1] += 1
            cons_omega[dat_idx + 1][land_grid_num + 1] -= 1
            cons_xi[dat_idx + 1][0] -= meas[i][2]
            
            # landmark flipx
            cons_omega[land_grid_num][dat_idx] -= 1
            cons_omega[land_grid_num][land_grid_num] += 1
            cons_xi[land_grid_num][0] += meas[i][1]
        
            # ladnmark flipy
            cons_omega[land_grid_num + 1][dat_idx + 1] -= 1
            cons_omega[land_grid_num + 1][land_grid_num + 1] += 1
            cons_xi[land_grid_num + 1][0] += meas[i][2]
        
    mu = np.linalg.inv(np.matrix(cons_omega))*np.array(cons_xi)
    
    return mu # return `mu`

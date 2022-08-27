# Job Sequencing Problem
# https://practice.geeksforgeeks.org/problems/job-sequencing-problem-1587115620/1



if __name__ == "__main__":
    N = 4
    Jobs = {(1,4,20),(2,1,10),(3,1,40),(4,1,30)}
    jobs = []
    for job in Jobs:
        jobs.append(job)
    jobs.sort(key=lambda x: -x[2])
    print(Jobs)
    max_deadline = 0
    for job in Jobs:
        if job[1]>max_deadline:
            max_deadline = job[1]
    
    deadline_arr = [-1 for i in range(max_deadline+1)]
    
    max_profit = 0
    max_jobs = 0

    for i in range(len(jobs)):
        curr_profit = jobs[i][2]
        curr_job_id = jobs[i][0]
        curr_deadline = jobs[i][1]
        for j in range(curr_deadline,0,-1):
            if curr_deadline>max_deadline:
                break
            if deadline_arr[j] == -1:
                deadline_arr[j] = curr_deadline
                max_profit+=curr_profit
                break
    print(deadline_arr)
    print(max_profit)

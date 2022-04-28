# Retrieve job results

This guide shows you how to view final job results after running a job.

## Before you begin

Throughout this guide we will assume that you have set the job you want to retrieve results as variable `job` by any of the following methods:

1. run a job using `QiskitRuntimeService.run()`. (TODO: link to how to run a job)
2. retrieve a job that has been ran before. (TODO: link to how to retrieve job)

## Check job status

You can only retrieve job results afer the job has been completed. To check the job status, you can run:

```python
job.status()
```

If it returns `<JobStatus.DONE: 'job has successfully run'>`, the job has been completed and you can proceed to retrieve job results.

## Retrieve job results

You can retrieve job results using:

```python
job.result()
```
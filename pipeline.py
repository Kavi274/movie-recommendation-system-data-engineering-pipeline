import subprocess

print("Starting Data Pipeline...")

# Step 1 Extract
print("Running Extract Step...")
subprocess.run(["python", "read_s3_data.py"])

# Step 2 Transform
print("Running Transform Step...")
subprocess.run(["python", "transform_data.py"])

# Step 3 Load
print("Running Load Step...")
subprocess.run(["python", "load_to_postgres.py"])

print("Pipeline completed successfully!")
import requests

url = "http://117.3.0.23:8543/api/auth-db/data/actual"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0YWJsZU5hbWUiOiJMaW5lIEN-fjIwfn4yOSIsImlhdCI6MTcyOTkwODY0NiwiZXhwIjozMzI1NTk1MTA0Nn0.Lx2d-hr0l9b7G4R06wjbNXbKPlfwNONJyHBVuF73lVQ",
}

# Dữ liệu cần gửi
payload = {"throughput": 150}

response = requests.post(url, json=payload, headers=headers)
if response.status_code == 201:
    print("Dữ liệu đã được chèn thành công")
else:
    print("Có lỗi xảy ra:", response.json())

from flask import Flask, render_template, jsonify

app = Flask(__name__)

PC = [
  {
    'id': 1,
    'cpu': 'Ryzen',
    'motherboard': 'Standard-ATX',
    'memory': '16GB DDR4 RAM',
    'storage': 'PCIe Gen 4.0 x4 NVME M.2 SSD 2TB',
    'gpu': 'NVIDIA GeForce RTX 4070 SUPER',
    'case': 'Lian Li LANCOOL 216 RGB',
    'psu': '800W 80+ gold'
  },
  {
    'id': 2,
    'cpu': 'Intel',
    'motherboard': 'Micro-ATX',
    'memory': '32GB DDR5 RAM',
    'storage': 'PCIe Gen 5.0 x4 NVME M.2 SSD 2TB',
    'gpu': 'NVIDIA GeForce RTX 4090',
    'case': 'Lian Li LANCOOL 216 RGB',
    'psu': '1000W 80+ gold'
  },
  {
    'id': 3,
    'cpu': 'Intel',
    'motherboard': 'Mini-ITX',
    'memory': '32GB DDR5 RAM',
    'storage': 'PCIe Gen 5.0 x4 NVME M.2 SSD 1TB',
    'gpu': 'NVIDIA GeForce RTX 4080',
    'case': 'Lian Li LANCOOL 216 RGB',
    'psu': '700W fully modular'
  },
  {
    'id': 4,
    'cpu': 'Qualcomm',
    'motherboard': 'Standard-ATX',
    'memory': '16GB DDR4 RAM',
    'storage': 'PCIe Gen 4.0 x4 NVME M.2 SSD 2TB',
    'gpu': 'NVIDIA GeForce RTX 4060 SUPER',
    'case': 'Lian Li LANCOOL 216 RGB',
    'psu': '700W 80+ gold'
  },
  {
    'id': 5,
    'cpu': 'Asus',
    'motherboard': 'Micro-ATX',
    'memory': '128GB DDR5 RAM',
    'storage': 'PCIe Gen 5.0 x4 NVME M.2 SSD 2TB',
    'gpu': 'NVIDIA GeForce RTX 4070',
    'case': 'Lian Li LANCOOL 216 RGB',
    'psu': '1000W 90+ gold'
  },
  {
    'id': 6,
    'cpu': 'Cyrix',
    'motherboard': 'Standard-ATX',
    'memory': '32GB DDR4 RAM',
    'storage': 'PCIe Gen 5.0 x4 NVME M.2 SSD 4TB',
    'gpu': 'NVIDIA GeForce RTX 4090 SUPER',
    'case': 'Lian Li LANCOOL 216 RGB',
    'psu': '800W 80+ gold'
  },
  {
    'id': 7,
    'cpu': 'Nvidia',
    'motherboard': 'Micro-ATX',
    'memory': '32GB DDR5 RAM',
    'storage': 'PCIe Gen 4.0 x4 NVME M.2 SSD 4TB',
    'gpu': 'NVIDIA GeForce RTX 4080',
    'case': 'Lian Li LANCOOL 216 RGB',
    'psu': '1000W 90+ gold'
  },
  {
    'id': 8,
    'cpu': 'Intel',
    'motherboard': 'Standard-ATX',
    'memory': '32GB DDR4 RAM',
    'storage': 'PCIe Gen 5.0 x4 NVME M.2 SSD 1TB',
    'gpu': 'NVIDIA GeForce RTX 4050',
    'case': 'Lian Li LANCOOL 216 RGB',
    'psu': '650W 80+ gold'
  }
]

@app.route("/")
def JpApp():
  return render_template('index.html', pc=PC)

@app.route("/pc")
def list_pc():
  return jsonify(PC)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


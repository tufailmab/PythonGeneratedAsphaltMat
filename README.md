<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Prony Series Fitting for Viscoelastic Materials</title>
</head>
<body>
  <h1>Prony Series Fitting for Viscoelastic Materials</h1>

  <p>This project provides a Python-based solution for fitting experimental relaxation modulus data to a Prony series model, commonly used for viscoelastic material simulations. The code also generates an <code>.inp</code> material file compatible with ABAQUS.</p>

  <h2>Features</h2>
  <ul>
    <li><strong>Curve Fitting:</strong> Fit experimental relaxation modulus data using a reduced-term Prony series.</li>
    <li><strong>Parameter Normalization:</strong> Ensures proper scaling of coefficients for reliable material models.</li>
    <li><strong>Automated ABAQUS File Generation:</strong> Outputs a ready-to-use <code>.inp</code> material file.</li>
    <li><strong>Visualization:</strong> Graphically compare experimental data and fitted curves.</li>
  </ul>

  <h2>Usage Instructions</h2>
  <ol>
    <li>Replace the sample data in the <code>data</code> variable with your experimental dataset.</li>
    <li>Run the script using:
      <pre><code>python prony_series_fit.py</code></pre>
    </li>
    <li>Review the generated file: <code>Python Generated Asphalt Material.inp</code></li>
    <li>Customize or extend the code as needed.</li>
  </ol>

  <h2>Requirements</h2>
  <p>The following Python packages are required:</p>
  <ul>
    <li>numpy</li>
    <li>scipy</li>
    <li>matplotlib</li>
  </ul>
  <p>Install dependencies using:</p>
  <pre><code>pip install numpy scipy matplotlib</code></pre>

  <h2>License</h2>
  <p>This project is licensed under the <strong>GNU General Public License v3.0 (GPLv3)</strong>.</p>
  <p>You are free to use, modify, and distribute this software under the terms of GPLv3. If you use this software in your work, please provide appropriate credit to the developer.</p>

  <h2>Developer Information</h2>
  <ul>
    <li><strong>Developer:</strong> Engr. Tufail Mabood</li>
    <li><strong>Contact:</strong> <a href="https://wa.me/+923440907874">WhatsApp</a></li>
    <li><strong>Note:</strong> This tool is open-source. Feel free to modify it and share improvements.</li>
  </ul>
</body>
</html>

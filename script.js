function checkUrine() {
  const color = document.getElementById("color").value;
  const frequency = parseInt(document.getElementById("frequency").value);
  let resultText = "";
  let resultClass = "";

  if (color === "Helder" && frequency >= 6) {
    resultText = "Top gehydrateerd!";
    resultClass = "helder";
  } else if (color === "Donker" || frequency < 4) {
    resultText = "Drink wat meer water.";
    resultClass = "donker";
  } else {
    resultText = "Redelijk, maar let op je vochtinname.";
    resultClass = "troebel";
  }

  const resultDiv = document.getElementById("result");
  resultDiv.style.display = "block";
  resultDiv.className = "result " + resultClass;
  document.getElementById("resultText").textContent = resultText;
}

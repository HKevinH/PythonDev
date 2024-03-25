function formDepositHidden() {
  document.getElementById("depositForm").style.display = "block";
}

function fetchAndUpdateTransactions(url, selector) {
  fetch(url)
    .then((response) => {
      if (!response.ok) {
        throw new Error("La solicitud ha fallado: " + response.statusText);
      }
      return response.json();
    })
    .then((data) => {
      const transactions = JSON.parse(data);
      const tbody = document.querySelector(selector);
      tbody.innerHTML = "";

      console.log(transactions);

      transactions.forEach((tr) => {
        const row = `<tr>
                       <td>${tr.fields.created_at}</td>
                       <td>${tr.fields.type}</td>
                       <td>$${tr.fields.value}</td>
                     </tr>`;
        tbody.innerHTML += row;
      });
    })
    .catch((error) => {
      console.error("Error durante la fetch:", error);
    });
}

document.addEventListener("DOMContentLoaded", function () {
  fetchAndUpdateTransactions("/get_transactions", ".table tbody");
});

document.addEventListener("DOMContentLoaded", function () {
  const selectField = document.getElementById("id_empresa");
  if (selectField) {
    const firstOption = selectField.options[0];
    firstOption.text = "Selecione a empresa";
  }
});

function addFieldsFromJSON(jsonData) {
    // Select the .card-body element
    var cardBody = document.querySelector(".card-body");

    // Select the fifth child of .card-body as the template for all other fields
    var template = cardBody.children[4].cloneNode(true);  // Index is 4 because indexing starts at 0

    // Reference to the last child element in .card-body where new elements will be inserted before
    var lastElement = cardBody.lastElementChild;

    Object.entries(jsonData).forEach(([key, value]) => {
        // Clone the template node
        var newFormGroup = template.cloneNode(true);

        // Update the label and input with new field information
        var label = newFormGroup.querySelector("label");
        var input = newFormGroup.querySelector("input");
        var allDivs = newFormGroup.querySelectorAll("div");

        // Set input attributes for number type input
        input.type = "number"; // Ensure it is set to number
        input.name = key;
        input.id = "id_" + key;
        input.value = value;
        input.removeAttribute("disabled");  // Remove disabled attribute if present

        // Set label attributes and text
        label.setAttribute('for', "id_" + key);
        label.innerHTML = key.charAt(0).toUpperCase() + key.slice(1).replace(/_/g, ' ') +
            label.innerHTML.substring(label.innerHTML.indexOf('<'));  // Keep the existing HTML, like the red star

        // Update help blocks if necessary
        allDivs.forEach(div => {
            if (div.classList.contains("help-block")) {
                div.innerHTML = "";  // Clear existing help texts or set to new ones
            }
        });

        // Insert the new form group just before the last element in the card-body
        cardBody.insertBefore(newFormGroup, lastElement);
    });
}

document.addEventListener("DOMContentLoaded", function() {
    additional_fields = document.querySelector('#id_additional_fields')
    let jsonObject = JSON.parse(additional_fields.value);
    addFieldsFromJSON(jsonObject);
    additional_fields.remove()
});
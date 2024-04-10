const input_btn = document.getElementById('input-btn');
const input_El = document.getElementById('text_input');

function getInputVal() {
    console.log(input_El.value);
}

input_btn.addEventListener("click", getInputVal);
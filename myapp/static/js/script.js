function displayMessage() {
    console.log("Hello World!");
}

document.getElementById("btn").addEventListener("click", () => {
    const inputValue = document.getElementById("one").value;
    document.getElementById('out').innerHTML = inputValue;
});
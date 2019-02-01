let quill = new Quill('#editor-container', {
  modules: {
    toolbar: [
      [{ header: [1, 2, false] }],
      ['bold', 'italic', 'underline'],
      ['image', 'code-block']
    ]
  },
  placeholder: 'Compose an epic...',
  theme: 'snow'  // or 'bubble'
});


let form = document.querySelector('form');
form.onsubmit = function() {
    // Populate hidden form on submit
    let content = document.querySelector('input[name=content]');
    content.value = quill.root.innerHTML;

    console.log("Submitted", $(form).serialize(), $(form).serializeArray());
};

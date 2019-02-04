hljs.configure({   // optionally configure hljs
  languages: ['javascript', 'c', 'python']
});


let quill = new Quill('#editor-container', {
  modules: {
      syntax: true,
    toolbar: [
      [{ header: [1, 2, false] }],
      ['bold', 'italic', 'underline'],
      ['image', 'code-block'],

    ]
  },
  placeholder: 'Compose an epic...',
  theme: 'snow',
});

var Image = Quill.import('formats/image');
class ImageBlot extends Image {
  static create(value) {
    let node = super.create(value);
    console.log(value);
    node.classList.add('ui');
    node.classList.add('fluid');
    node.classList.add('image');
    return node;
  }
}
Quill.register(ImageBlot, true);


let form = document.querySelector('form');
form.onsubmit = function() {
    // Populate hidden form on submit
    let content = document.querySelector('input[name=content]');
    content.value = quill.root.innerHTML;

    console.log("Submitted", $(form).serialize(), $(form).serializeArray());
};

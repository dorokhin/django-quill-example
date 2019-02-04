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


let form = document.querySelector('form');
form.onsubmit = function() {
    // Populate hidden form on submit
    let content = document.querySelector('input[name=content]');
    content.value = quill.root.innerHTML;

    console.log("Submitted", $(form).serialize(), $(form).serializeArray());
};

var toolbar = quill.getModule('toolbar');
toolbar.addHandler('image', imageHandler);


function imageHandler(a, b) {
    console.log(a, b);
    var range = this.quill.getSelection();
    var that = this;

    var input = document.createElement('input');
    input.type = 'file';

    input.onchange = e => {
       var file = e.target.files[0];
       var reader = new FileReader();
       reader.readAsDataURL(file);

       reader.onload = readerEvent => {
          var content = readerEvent.target.result;
          that.quill.insertEmbed(range.index, 'image', content, Quill.sources.USER);
       }
    };
    input.click();
}

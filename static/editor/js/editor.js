

let quill = new Quill('#editor-container', {
  modules: {
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

       // getting a hold of the file reference
       var file = e.target.files[0];

       // setting up the reader
       var reader = new FileReader();
       reader.readAsDataURL(file); // this is reading as data url

       // here we tell the reader what to do when it's done reading...
       reader.onload = readerEvent => {
          var content = readerEvent.target.result; // this is the content!
          that.quill.insertEmbed(range.index, 'image', content, Quill.sources.USER);
       }

    };

    input.click();
}

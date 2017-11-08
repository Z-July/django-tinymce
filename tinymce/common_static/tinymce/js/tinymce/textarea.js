/**
 * Created by Administrator on 2016/4/10 0010.
 */
tinymce.init({
    selector: "textarea",
    themes: "modern",
    menubar: false,
    convert_urls: false,
    height: 450,
    plugins: [
        'advlist autolink lists link image charmap print preview hr anchor pagebreak',
        'searchreplace wordcount visualblocks visualchars code fullscreen',
        'insertdatetime media nonbreaking save table contextmenu directionality',
        'emoticons template paste textcolor colorpicker textpattern imagetools',
        "link imageupload"
    ],
    toolbar: "undo redo | imageupload link | bold italic | styleselect fontselect fontsizeselect | bullist numlist outdent indent | alignleft aligncenter alignright alignjustify | print preview media | forecolor backcolor emoticons",
    content_css: [
    '//fast.fonts.net/cssapi/e6dc9b99-64fe-4292-ad98-6974f93cd2a2.css',
    '//www.tinymce.com/css/codepen.min.css'
    ],
    imageupload_url: '/upload_img/',
    language:'zh_CN'
});
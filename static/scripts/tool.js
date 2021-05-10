
function mobileMenu() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

function toKhNum(number) {
    var khNum = {'0':'០', '1':'១', '2':'២', '3':'៣', '4':'៤', '5':'៥', '6':'៦', '7':'៧', '8':'៨', '9':'៩'};
    var stringNum = number.toString();
    var khString = '';
   
    for(var i in stringNum){
      var char = stringNum.charAt(i);
      khString += khNum[char];
    }
   
    return khString;
  }
  
  function getKhDate (rawDate){
    var KhmerDays = ['អាទិត្យ', 'ច័ន្ទ', 'អង្គារ', 'ពុធ', 'ព្រហស្បតិ៍', 'សុក្រ', 'សៅរ៍'];
    var KhmerMonths = ['មករា', 'កុម្ភៈ', 'មិនា', 'មេសា', 'ឧសភា', 'មិថុនា', 'កក្កដា', 'សីហា', 'កញ្ញា', 'តុលា', 'វិច្ឆិកា', 'ធ្នូ'];
    var date = new Date(rawDate);
    var month = date.getMonth();
    var day = date.getDay();
    var daym = toKhNum(date.getDate());
    var year = toKhNum(date.getFullYear());
    var time = date.toLocaleTimeString();
    return ('ថ្ងៃ '+ KhmerDays[day]+' ទី '+daym+' '+KhmerMonths[month]+' '+year)
  }

  function checkTime(i) {
    if (i < 10){i = "0" + i};  
    return i;
  }

  function clock(){
    var period = 'ព្រឹក';
    var today = new Date();
    var h = today.getHours();
    if(h>12){
      h = h-12;
      period = 'ល្ងាច';
    }
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
  
    document.getElementById('kh-clock').innerHTML = toKhNum(h) + " : " + toKhNum(m) + " : " + toKhNum(s)+' '+period;
    var t = setTimeout(clock, 500);
  }
  
function straxFun(){
    alert("Now you will be redirected to a Third-party website to buy strax where you have to login/register again into their respective system,"+"            "+"Press OK to continue.")
    window.open("https://www.binance.com/en-IN/trade/STRAX_USDT", "_blank");
}

function copyFun(){
    var address=document.getElementById('add').innerHTML;
    navigator.clipboard.writeText(address);
    alert("Your " +address+" is copied to your clipboard.");

}



function txn(){
   alert("");
   window.open("");
}
const BASE_URL="https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies";

const dropdowns=document.querySelectorAll(".dropdown select");
const result=document.querySelector(".msg");
const btn=document.querySelector(".convert");
const fromVar=document.querySelector(".from select");
const toVar=document.querySelector(".to select");

for(let select of dropdowns){
    for(country in countryList){
        let newDrop=document.createElement("option");
        newDrop.innerText=country;
        newDrop.value=country;
        if(select.name==="from"&&country==="USD"){
            newDrop.selected=select;
        }  
        else if(select.name==="to"&&country==="INR"){
            newDrop.selected=select;
        }
        select.append(newDrop)
    }

    select.addEventListener("change",(evt)=>{
        updateFlag(evt.target);
    });
}

const amountCalculator=async ()=>{
    let amt=document.querySelector(".amount input");
    let amtVal=amt.value;
    if(amtVal===""||amtVal<1){
        amtVal=1;
    }
    let fromVal=fromVar.value;
    let toVal=toVar.value;
    const url=`${BASE_URL}/${fromVal.toLowerCase()}.json`;
    let response=await fetch(url);
    let data=await response.json();
    let rate=data[fromVal.toLowerCase()][toVal.toLowerCase()];
    let finalAmt=amtVal*rate;
    result.innerText=`${amtVal} ${fromVal} = ${finalAmt.toFixed(2)} ${toVal}`;
};

function updateFlag(element){
    let curCode=countryList[element.value];
    console.log(curCode);
    let newSrc=`https://flagsapi.com/${curCode}/flat/64.png`;
    let img=element.parentElement.querySelector("img");
    img.src=newSrc;
}

btn.addEventListener("click",(evt)=>{
    evt.preventDefault();
    amountCalculator();
});

window.addEventListener("load", () => {
    amountCalculator();
});



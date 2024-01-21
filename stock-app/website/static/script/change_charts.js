function changeIndicatorsChart(number){
    if(number==="first"){
        document.getElementById("indicatorsFirstBlock").style.display="block";
        document.getElementById("indicatorsSecondBlock").style.display="none";
        document.getElementById("indicatorsFourthBlock").style.display="none";
    }
    else if(number==="second"){
        document.getElementById("indicatorsFirstBlock").style.display="none";
        document.getElementById("indicatorsSecondBlock").style.display="block";
        document.getElementById("indicatorsFourthBlock").style.display="none";
    }
    else if(number==="fourth"){
        document.getElementById("indicatorsFirstBlock").style.display="none";
        document.getElementById("indicatorsSecondBlock").style.display="none";
        document.getElementById("indicatorsFourthBlock").style.display="block";
    }
}

function changeCommoditiesChart(number){
    if(number==="zero"){
        document.getElementById("commoditiesZeroBlock").style.display="block";
        document.getElementById("commoditiesFirstBlock").style.display="none";
        document.getElementById("commoditiesSecondBlock").style.display="none";
        document.getElementById("commoditiesThirdBlock").style.display="none";
    }
    else if(number==="first"){
        document.getElementById("commoditiesZeroBlock").style.display="none";
        document.getElementById("commoditiesFirstBlock").style.display="block";
        document.getElementById("commoditiesSecondBlock").style.display="none";
        document.getElementById("commoditiesThirdBlock").style.display="none";
    }
    else if(number==="second"){
        document.getElementById("commoditiesZeroBlock").style.display="none";
        document.getElementById("commoditiesFirstBlock").style.display="none";
        document.getElementById("commoditiesSecondBlock").style.display="block";
        document.getElementById("commoditiesThirdBlock").style.display="none";
    }
    else if(number==="third"){
        document.getElementById("commoditiesZeroBlock").style.display="none";
        document.getElementById("commoditiesFirstBlock").style.display="none";
        document.getElementById("commoditiesSecondBlock").style.display="none";
        document.getElementById("commoditiesThirdBlock").style.display="block";
    }
}
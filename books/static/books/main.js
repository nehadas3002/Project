document.addEventListener('DOMContentLoaded', function() {
    
    load_default_2(); 

    document.querySelector('#drop-down-2').onclick = function() {
        if (document.querySelector('#rating-info').style.display === 'none') {
            document.querySelector('#rating-info').style.display = 'block'; 
        } else if (document.querySelector('#rating-info').style.display === 'block') {
            document.querySelector('#rating-info').style.display = 'none';
        }
         
    }

    const first = document.getElementById('first')
    const second = document.getElementById('second')
    const third = document.getElementById('third')
    const fourth = document.getElementById('fourth')
    const fifth = document.getElementById('fifth')
    const form = document.querySelector('.rate-form')

    let div = document.querySelector('#alert')

    const handleSelect = (selection) => {
        switch(selection) {
            case 'first': {
                first.classList.add('checked')
                second.classList.remove('checked')
                third.classList.remove('checked')
                fourth.classList.remove('checked')
                fifth.classList.remove('checked')
                return
    
            }
            case 'second': {
                first.classList.add('checked')
                second.classList.add('checked')
                third.classList.remove('checked')
                fourth.classList.remove('checked')
                fifth.classList.remove('checked')
                return
            }

            case 'third': {
                first.classList.add('checked')
                second.classList.add('checked')
                third.classList.add('checked')
                fourth.classList.remove('checked')
                fifth.classList.remove('checked')
                return
            }

            case 'fourth': {
                first.classList.add('checked')
                second.classList.add('checked')
                third.classList.add('checked')
                fourth.classList.add('checked')
                fifth.classList.remove('checked')
                return
            }

            case 'fifth': {
                first.classList.add('checked')
                second.classList.add('checked')
                third.classList.add('checked')
                fourth.classList.add('checked')
                fifth.classList.add('checked')
                return
            }
        
        }
    }

    arr = [first, second, third, fourth, fifth]
    
    arr.forEach(item=> item.addEventListener('mouseover', (event)=> {
        handleSelect(event.target.id)
    }))

})



function load_default_2() {
    document.querySelector('#view-rates').style.display = 'grid';
    document.querySelector('#rating-info').style.display = 'none';
}


document.addEventListener('DOMContentLoaded', function() {


    
    
    document.querySelector('#drop-down').onclick = function() {
        if (document.querySelector('#adding-div').style.display === 'none') {
            document.querySelector('#adding-div').style.display = 'block'; 
        } else if (document.querySelector('#adding-div').style.display === 'block') {
            document.querySelector('#adding-div').style.display = 'none';
        }
        
         
    }

    load_default(); 
})

function load_default() {
    document.querySelector('#add-title').style.display = 'grid';
    document.querySelector('#adding-div').style.display = 'none'; 


}



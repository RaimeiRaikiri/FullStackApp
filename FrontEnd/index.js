const form = document.querySelector("#form");
form.addEventListener("submit", function(){
    create_contact();
});
//fetch("http://127.0.0.1:5000/create_contact", payload)

async function create_contact()
{
   const firstName = document.querySelector("#form>fieldset>div>#firstName");
   const lastName = document.querySelector("#form>fieldset>div>#lastName");
   const email = document.querySelector("#form>fieldset>div>#email");
   
   const payload = {
    "method": "POST",
    "headers": {
        "Content-Type": "application/json"
    },
    "body": JSON.stringify({
        "firstName": firstName.value,
        "lastName": lastName.value,
        "email": email.value
   })
   }
   
   const response = fetch(base_url+"/create_contact", payload);
   

}

const base_url = "http://127.0.0.1:5000"
function delete_contact(base_url){
    const payload = {
        "method": "DELETE",
        "header": {
            "Content-Type": "application/json"
        }
    }
    fetch(base_url+"/delete_contact/1", payload)
}

function check_contacts(base_url){
    fetch(base_url+"/contacts");
}

function update_contact(base_url){
    const payload = {
        "method": "PATCH",
        "headers": {
            "Content-Type": "application/json"
        },
        "body": JSON.stringify(
            {
                "firstName": "michael",
                "lastName": "scutts"
            }
        )
    }

    fetch(base_url+"/update_contact/1", payload)
}

const payload = {
    "method": "POST",
    "headers": {
        "Content-Type": "application/json"
    },
    "body": JSON.stringify(
        {
            "firstName": "Jake",
            "lastName": "Smith",
            "email": "jakesmith@gmail.com"
        }
    )
}
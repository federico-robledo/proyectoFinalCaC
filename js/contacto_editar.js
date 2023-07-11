console.log(location.search) // lee los argumentos pasados a este formulario
var id_contacto = location.search.substr(4)
console.log(id_contacto)
const { createApp } = Vue
createApp({
    data() {
        return {
            id_contacto: 0,
            nombre: "",
            apellido: "",
            correo_electronico: "",
            telefono: 0,
            direccion: "",
            // url:'http://promero.pythonanywhere.com/productos/'+id,
            url:'https://frobledo.pythonanywhere.com/index/'+id_contacto,
            // url: 'http://localhost:5000/index/'+id_contacto,
        }
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {

                    console.log(data)
                    this.id_contacto = data.id_contacto
                    this.nombre = data.nombre;
                    this.apellido = data.apellido
                    this.correo_electronico = data.correo_electronico
                    this.telefono = data.telefono
                    this.direccion = data.direccion
                })
                .catch(err => {
                    console.error(err);
                    this.error = true
                })
        },
        modificar() {
            let contacto = {
                nombre: this.nombre,
                apellido: this.apellido,
                correo_electronico: this.correo_electronico,
                telefono: this.telefono,
                direccion: this.direccion
            }
            var options = {
                body: JSON.stringify(contacto),
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            fetch(this.url, options)
                .then(function () {
                    alert("Registro modificado")
                    window.location.href = "../index.html";
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Modificar")
                })
        }
    },
    created() {
        this.fetchData(this.url)
    },
}).mount('#app')
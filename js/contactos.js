const { createApp } = Vue
createApp({
    data() {
        return {
            contactos: [],
            // url: 'http://localhost:5000/index',
            // si el backend esta corriendo local usar localhost 5000(si no lo subieron a pythonanywhere)
            // url:'http://promero.pythonanywhere.com/productos/', // si ya lo subieron a pythonanywhere
            url:'https://frobledo.pythonanywhere.com/index', // si ya lo subieron a pythonanywhere
            error: false,
            cargando: true,
            /*atributos para guardar los valores del formulario */
            id_contacto: 0,
            nombre: "",
            apellido: "",
            correo_electronico: "",
            telefono: 0,
            direccion: "",
        }
    },
    methods: {
        fetchData(url) {
            fetch(url)
                .then(response => response.json())
                .then(data => {
                    this.contactos = data;
                    this.cargando = false
                })
                .catch(err => {
                    console.error(err);
                    this.error = true
                })
        },
        eliminar(contacto) {
            const url = this.url + '/' + contacto;
            var options = {
                method: 'DELETE',
            }
            fetch(url, options)
                .then(res => res.text()) // or res.json()
                .then(res => {
                    location.reload();
                })
        },
        grabar() {
            let contacto = {
                nombre: this.nombre,
                apellido: this.apellido,
                correo_electronico: this.correo_electronico,
                telefono: this.telefono,
                direccion: this.direccion
            }
            var options = {
                body: JSON.stringify(contacto),
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                redirect: 'follow'
            }
            fetch(this.url, options)
                .then(function () {
                    alert("Registro grabado")
                    window.location.href = "../index.html";
                })
                .catch(err => {
                    console.error(err);
                    alert("Error al Grabar")
                })
        }
    },
    created() {
        this.fetchData(this.url)
    },
}).mount('#app')
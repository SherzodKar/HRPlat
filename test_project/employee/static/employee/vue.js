new Vue({
    delimiters: ['[[', ']]'],
    el:'title',
    data:{
        employeeinfo: 'Employee Profile'
    }
});
new Vue({
    delimiters: ['[[', ']]'],
    el:'.navbar-brand',
    data:{
        emp_home: 'Employee Information'
    }
});
new Vue({
    delimiters: ['[[', ']]'],
    el:'header',
    data:{
        home: 'Home',
        profile: 'Profile',
        logout: 'Logout',
        login: 'Login',
        register: 'Register'
    }
});

var app = new Vue({
    delimiters: ['[[', ']]'],
    el: '.game',
    data: {
        seen1: true,
        seen2: false,
        seen3: false,
        personal: 'Personal Information',
        background: 'Background Information',
        employment: 'Employment Information',
        notes: 'Notes'
    }
});  
new Vue({
    delimiters: ['[[', ']]'],
    el: '.drop',
    data: {
        intro: false
    }
})  


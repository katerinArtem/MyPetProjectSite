(this.webpackJsonpfrontend=this.webpackJsonpfrontend||[]).push([[0],{40:function(e,t,n){},42:function(e,t,n){},43:function(e,t,n){},44:function(e,t,n){},45:function(e,t,n){"use strict";n.r(t);var c=n(2),s=n.n(c),r=n(16),i=n.n(r),j=n(17),a=n(3),l=n.n(a),o=(n(6),n(40),n(0)),d=function(){return Object(o.jsx)("div",{className:"fixed-top _navbar",id:"navMenu",children:Object(o.jsxs)("div",{className:"itemlist",children:[Object(o.jsx)("a",{className:"linkItem",href:"{% url 'main:home' %}",children:Object(o.jsx)("div",{children:"Home"})}),Object(o.jsx)("a",{className:"linkItem",href:"{% url 'main:posts' %}",children:Object(o.jsx)("div",{children:"Posts"})}),Object(o.jsx)("a",{className:"linkItem",href:"{% url 'main:features' %}",children:Object(o.jsx)("div",{children:"Features"})}),Object(o.jsx)("form",{className:"formItem",children:"Input"}),Object(o.jsxs)("div",{className:"_dropdown",children:[Object(o.jsx)("button",{className:"_dropbtn",children:"Username"}),Object(o.jsxs)("div",{className:"_dropdown-content",style:{right:0},children:[Object(o.jsx)("a",{href:"{% url 'main:profile_update' %}",children:"Profile"}),Object(o.jsx)("a",{href:"{% url 'main:profile_posts' %}",children:"Your posts"}),Object(o.jsx)("a",{href:"{% url 'main:profile_dialogs' %}",children:"Dialogs"}),Object(o.jsx)("a",{href:"{% url 'logout' %}",children:"Logout"}),Object(o.jsx)("a",{href:"{% url 'main:home'%}admin/",children:"Admin Panel"})]})]}),Object(o.jsx)("a",{className:"imglinkItem",href:"{% url 'main:profile_update' %}",children:"Image"}),Object(o.jsx)("button",{className:"btn btn-outline-light",id:"Login",type:"button",children:"Login"}),Object(o.jsx)("button",{className:"btn btn-warning ",id:"Sign-up",type:"button",children:"Sign-up"})]})})},b=(n(42),function(){return Object(o.jsxs)("div",{className:"background_content",children:[Object(o.jsx)("hr",{}),Object(o.jsx)("hr",{}),Object(o.jsx)("hr",{}),Object(o.jsx)("hr",{}),Object(o.jsx)("hr",{}),Object(o.jsx)("hr",{}),Object(o.jsx)("strong",{children:"Content"})]})}),h=(n(43),function(){return Object(o.jsx)("div",{className:"footer_color",children:Object(o.jsx)("a",{href:"#",children:Object(o.jsx)("h2",{children:"some footer some footer"})})})});n(44);var u=function(){var e=Object(c.useState)([]),t=Object(j.a)(e,2),n=t[0],s=t[1];return n=n,Object(c.useEffect)((function(){l()({method:"GET",url:"http://127.0.0.1:8000/api/posts/"}).then((function(e){s(e.data)}))}),[]),Object(o.jsx)("div",{className:"App",children:Object(o.jsxs)("div",{className:"wrapper",children:[Object(o.jsx)(d,{}),Object(o.jsx)(b,{}),Object(o.jsx)(h,{})]})})};i.a.render(Object(o.jsx)(s.a.StrictMode,{children:Object(o.jsx)(u,{})}),document.getElementById("root"))}},[[45,1,2]]]);
//# sourceMappingURL=main.0e65c36f.chunk.js.map
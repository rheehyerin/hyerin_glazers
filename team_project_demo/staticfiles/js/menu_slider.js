(function(window, document){
            var menuBottom = document.getElementById( 'cbp-spmenu-s4' ),
                showBottom = document.getElementById( 'showBottom' ),
                body = document.body;

            showBottom.onclick = function() {
                classie.toggle( this, 'active' );
                classie.toggle( menuBottom, 'cbp-spmenu-open' );
                disableOther( 'showBottom' );
            };

            function disableOther( button ) {
                if( button !== 'showBottom' ) {
                    classie.toggle( showBottom, 'disabled' );
                }
            }
        }
    )(window);






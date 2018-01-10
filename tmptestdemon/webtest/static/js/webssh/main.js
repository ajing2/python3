function openTerminal(options) {
    var client = new WSSHClient();
    var term = new Terminal({cols: 200, rows: 80, screenKeys: true, useStyle: true});
    term.on('data', function (data) {
        /*term实时监控输入的数据，并且websocket把实时数据发送给后台*/
        client.sendClientData(data);
    });
    term.open();
    // term.open(document.getElementById('container-terminal'));//屏幕将要在哪里展示，就是屏幕展示的地方
    $('.terminal').detach().appendTo('#term');
    $("#term").show();
    term.write('Connecting...');
    client.connect({
        onError: function (error) {
            term.write('Error: ' + error + '\r\n');
            console.debug('error happened');
        },
        onConnect: function () {
            client.sendInitData(options);
            client.sendClientData('\r');
            console.debug('connection established');
        },
        onClose: function () {
            term.write("\rconnection closed")
            console.debug('connection reset by peer');
            $('term').hide()
        },
        onData: function (data) {
            term.write(data);
            console.debug('get data:' + data);
        }
    })
}

var charWidth = 6.2;
var charHeight = 15.2;

/**
 * for full screen
 * @returns {{w: number, h: number}}
 */
function getTerminalSize() {
    var width = window.innerWidth;
    var height = window.innerHeight;
    return {
        w: Math.floor(width / charWidth),
        h: Math.floor(height / charHeight)
    };
}


function store(options) {
    window.localStorage.host = options.host
    window.localStorage.port = options.port
    window.localStorage.username = options.username
    window.localStorage.ispwd = options.ispwd;
    window.localStorage.secret = options.secret
}

function check() {
    return validResult["host"] && validResult["port"] && validResult["username"];
}

function connect() {
    // var remember = $("#remember").is(":checked")
    var options = {
        host: $("#host").val(),
        port: $("#port").val(),
        username: $("#username").val(),
        password: $("#password").val(),
        // ispwd: $("input[name=ispwd]:checked").val(),
        // secret: $("#secret").val(),
    }
    // if (remember) {
    //     store(options)
    // }
    openTerminal(options);
    if (check()) {
        openTerminal(options)
    } else {
        for (var key in validResult) {
            if (!validResult[key]) {
                alert(errorMsg[key]);
                break;
            }
        }
    }
}
import {white, pinkA200} from 'material-ui/styles/colors';


const sideBarWidth = 300;
const sideBarHeight = 200;

const Style = {
    header: {
        span: {
            paddingLeft: "20px"
        },

        link: {
            color: white,
            textColor: white,
            textDecoration: "none",
            cursor: "pointer"
        },
        
        activeLink: {
            color: pinkA200
        }
    },
    
    sideBarAvatar: {
        root: {
            display: 'flex',
            flexWrap: 'wrap',
            justifyContent: 'space-around'
        },
        
        gridList: {
            width: sideBarWidth,
            height: sideBarHeight,
            overflowY: 'auto'
        },
        gridListCellHeight: sideBarHeight
    },

    nemuItem: {
        textDecoration: "none",
        cursor: "pointer",
        color: "rgba(0, 0, 0, 0.87)"
    },

    drawler: {
        width: sideBarWidth
    },

    dialog: {
        width: "500px"
    },
    
    textAlignCenter: {
        textAlign: "center"
    }

};


export default Style;

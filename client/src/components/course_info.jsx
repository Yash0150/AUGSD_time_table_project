import React from 'react'
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import Typography from '@material-ui/core/Typography';
import TextField from '@material-ui/core/TextField';
import styled from 'styled-components';


const useStyles = makeStyles(theme =>({
    root: {
        textAlign: 'center',
        width: '200%',
        ...theme.typography.button,
        backgroundColor: theme.palette.background.paper,
        padding: theme.spacing(1),
        '& > *': {
            margin: theme.spacing(1),
            width: '25ch',
          },
    },
    heading: {
        marginBottom: 22,
    },
  }));

  const styles = {
    card_content: {
        margin: 'auto',
        width: '100%',
    },
    text_field: {
        margin: 'auto',
    }
  };

  const Form = styled.form`
    display: flex;
    flex-direction: column;
    margin: auto;
    width: 100%;
    justify-content: center;
  `;


export default function CourseInfo() {
    const classes = useStyles();
    return (
        <Card className={classes.root}>
        <CardContent style={styles.card_content}>
            <Typography variant="h5" className={classes.heading} >
                Course Info 
            </Typography>
            <Form className={classes.root} noValidate>
                <TextField id="standard-basic" label="lectures" style={styles.text_field} />
                <TextField id="standard-basic" label="tutorials" style={styles.text_field}  />
                <TextField id="standard-basic" label="practicals" style={styles.text_field}  />
                <TextField id="standard-basic" label="No. of students" style={styles.text_field}  />
                <TextField id="standard-basic" label="IC" style={styles.text_field}  />
                <TextField id="standard-basic" label="Max Strength" style={styles.text_field}  />
            </Form>
        </CardContent>
        </Card>
    )
}

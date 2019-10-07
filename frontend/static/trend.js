"use strict";

function drawchart() {
  axios.all([
    axios.all(app.objs.slice(0, 10).map(i => (
      axios.post('/admin/submission/', {
        method: 'get_user_history',
        args: {user: i.user},
      })
    ))),
    axios.post('/admin/trigger/', {method: 'get_all'}),
  ]).then(([user_reqs, {data: {value: triggers}}]) => {
    let starttime = triggers.find(i => i.state);
    let endtime = [...triggers].reverse().find(i => !i.state);
    if (!endtime || endtime > new Date()) {
      endtime = new Date();
    }
    let data = user_reqs.map(({data: {value: history}}, i) => {
      let points = history.map(i => ({x: i.time, y: i.score}));
      points.unshift({x: starttime, y: 0});
      points.push({x: endtime, y: points[points.length-1].y});
      return {
        type: 'stepLine',
        name: app.users[app.objs[i].user],
        showInLegend: true,
        dataPoints: points,
        markerSize: 0,
      };
    });
    new CanvasJS.Chart('chart', {
      legend: {
        verticalAlign: "top",
        horizontalAlign: "center",
      },
      toolTip: {
        content: "{name}: {y}",
      },
      data: data,
      animationEnabled: true,
      zoomEnabled: true,
      exportEnabled: true,
      axisX: {
        valueFormatString: "MM-DD HH:mm",
        labelAngle: -50,
        crosshair: {
          enabled: true,
        },
      },
    }).render();
  });
}
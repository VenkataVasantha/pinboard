$(document).ready(function(){

  var column_index, columns, columns_height, container, i, j, k, len, max_height, sp, space, tile, tiles, v, width;

  tiles = $('.tiles .t');

  container = $('.tiles').width();

  width = $('.tiles .t:first').width();

  columns_height = {};

  columns = Math.floor(container / width);

  space = container % width;

  space = space / (columns - 1);

  for (i = j = 0, len = tiles.length; j < len; i = ++j) {
    tile = tiles[i];
    column_index = i % columns;
    if (columns_height[column_index] == null) {
      columns_height[column_index] = 0;
    }
    sp = (function() {
      switch (column_index) {
        case 0:
          return 0;
        case columns:
          return 0;
        default:
          return space * column_index;
      }
    })();
    $(tile).css({
      top: columns_height[column_index],
      left: (column_index * width) + sp
    });
    columns_height[column_index] += $(tile).height() + space;
  }

  max_height = 0;

  for (k in columns_height) {
    v = columns_height[k];
    if (v > max_height) {
      max_height = v;
    }
  }

  $('.tiles').height(max_height - space);
});


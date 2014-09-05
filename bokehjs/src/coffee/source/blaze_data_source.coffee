define [
  "underscore"
  "backbone"
  "common/has_properties"
  "common/logging"
  "range/range1d"
  "range/data_range1d"

], (_, Backbone, HasProperties, Logging, Range1d, DataRange1d, server_data_source) ->

  logger = Logging.logger

  #maybe generalize to ajax data source later?
  class BlazeDataSource extends HasProperties
    type: 'BlazeDataSource'

    update : (column_data_source) ->
      $.ajax(
        dataType: 'json'
        url : @get('data_url')
        data : JSON.stringify(@get('expr'))
        xhrField :
          withCredentials : true
        method : 'POST'
        contentType : 'application/json'
      ).done((data) ->
        columns_of_data = _.zip.apply(_, data.data)
        data_dict = {}
        for colname, idx in data.names
          data_dict[colname] = columns_of_data[idx]
        orig_data = _.clone(column_data_source.get('data'))
        _.extend(orig_data, data_dict)
        column_data_source.set('data', orig_data)
      )

  class BlazeDataSources extends Backbone.Collection
    model: BlazeDataSource
    defaults:
      url : ""
      expr : null

  return {
    "Model": BlazeDataSource,
    "Collection": new BlazeDataSources()
  }

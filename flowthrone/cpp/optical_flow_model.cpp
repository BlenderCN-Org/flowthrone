#include "optical_flow_model.h"
#include "flowthrone.pb.h"
#include "optical_flow_tf_model.h"
#include "io.h"

namespace flowthrone {

std::unique_ptr<OpticalFlowModel> OpticalFlowModel::Create(
    const google::protobuf::Message& message) {
  const google::protobuf::Message* ptr = &message;
  if (dynamic_cast<const OpticalFlowTensorFlowModelOptions*>(ptr)) {
    auto opts = dynamic_cast<const OpticalFlowTensorFlowModelOptions*>(ptr);
    return std::make_unique<OpticalFlowTensorFlowModel>(*opts);
  }
  LOG(FATAL) << "Could not interpret the passed protobuf message as one of "
                "the types that can be used to instantiate OpticalFlowModel.";
  // That's all she wrote!
  return nullptr;
}

std::unique_ptr<OpticalFlowModel> OpticalFlowModel::Create(
    const std::string& filename) {
  // We cannot instantiate google::protobuf::Message (it's abstract), so
  // unfortunately if/else clauses for instantiating the derived class have to
  // be repeated here with a different flavour.
  CHECK(!filename.empty())
      << "You passed an empty string instead of a valid filename while trying "
         "to instantiate OpticalFlowModel.";

  OpticalFlowTensorFlowModelOptions tf_options;
  if (ParseTextProtoFromFile(filename, &tf_options)) {
    return std::make_unique<OpticalFlowTensorFlowModel>(tf_options);
  }
  LOG(FATAL) << "Provided filename " << filename
             << " does not contain a valid "
                "pbtxt configuration that can be parsed to instantiate "
                "OpticalFlowModel. Maybe there is a syntax error?";
  // That's all she wrote!
  return nullptr;
}

}  // namespace flowthrone

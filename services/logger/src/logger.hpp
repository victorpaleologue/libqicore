#ifndef QICORE_LOGGER_HPP
# define QICORE_LOGGER_HPP

# include <qi/log.hpp>
# include <qitype/anyobject.hpp>
# include <boost/shared_ptr.hpp>

QI_TYPE_ENUM_REGISTER(qi::LogLevel)

struct Message
{
  std::string source;
  qi::LogLevel level;
  qi::os::timeval timestamp;
  std::string category;
  std::string location;
  std::string message;
};

QI_TYPE_STRUCT_REGISTER(::Message, source, level, timestamp, category, location, message);

class LoggerProxy;
typedef boost::shared_ptr<LoggerProxy> LoggerProxyPtr;

// Register local logger to service
void registerToLogger(LoggerProxyPtr logger);

#endif // !QICORE_LOGGER_HPP
